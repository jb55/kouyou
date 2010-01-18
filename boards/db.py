from pymongo.connection import Connection
from pymongo.collection import ObjectId
import pymongo
from datetime import datetime
from kouyou.boards.models import Board, Post

LIMIT_AMOUNT = 10
NUM_PAGES = 2

conn = Connection()
database = conn.kouyou

def get_database():
  return database

class BoardManager():
  def __init__(self):
    self.boards = get_database().boards
    self.posts = get_database().posts

  def increase_post_count(self, board_code):
    self.boards.update(
      {'board_code': board_code}, 
      {'$inc': {'count': 1}})
    return self.get_board(board_code)

  def get_board_id(self, board_code):
    board = self.boards.find_one({'board_code': board_code}, fields=['board_id'])
    if board != None:
      return board["board_id"]
    return None

  def get_board(self, board_code):
    board = self.boards.find_one({'board_code': board_code})
    if board != None:
      return Board(board)
    return None

  def get_boards(self):
    boards = list(self.boards.find())
    boards_obj = [Board(b) for b in boards]
    return boards_obj

  def get_thread(self, thread_id):
    return Post(self.posts.find_one({'_id': ObjectId(str(thread_id))}))

  def get_post(self, post_id):
    return Post(self.posts.find_one({'id': post_id}))

  def get_posts(self, boardid, page=1):
    start_pos = (page-1) * LIMIT_AMOUNT
    end_pos = start_pos + LIMIT_AMOUNT
    latest_posts = self.posts.find({'board': boardid,})
      .sort('bumped_at', pymongo.DESCENDING)[start_pos:end_pos]
    posts = [Post(post) for post in latest_posts]
    return posts

  def archive_threads(self, boardid):
    start_pos = (NUM_PAGES * LIMIT_AMOUNT)
    dying = self.posts.find(
      {'board': boardid, 'dead': {'$exists': False}}, fields=[])
        .sort('bumped_at', pymongo.DESCENDING)[start_pos:]

    dying_threads = [thread["_id"] for thread in dying]
    if len(dying_threads) > 0:
      self.posts.update({'_id': {'$in': dying_threads}}, {'$set': {'dead': 1}})

  def can_bump_thread(self, thread_id):
    spec = {'_id': ObjectId(str(thread_id))}
    thread = Post(self.posts.find_one(spec, fields=Post.bump_fields))
    return thread.can_bump()

  def insert_post(self, post, board_code=None, thread_id=None):
    if not post.is_valid():
      return None
    board = self.increase_post_count(board_code)
    self.archive_threads(board.board_id)

    post.id = board.count
    post.created_at = datetime.utcnow()
    if thread_id != None:
      # reply
      spec = {'_id': ObjectId(str(thread_id))}
      self.posts.update(spec, {'$push': {'replies': post.as_dict()}})
      if self.can_bump_thread(thread_id):
        self.posts.update(spec, {'$set': {'bumped_at': datetime.utcnow()}})
    else:
      post.board = board.board_id
      if post.can_bump():
        post.bumped_at = datetime.utcnow()
      self.posts.insert(post.as_dict())

    return id
