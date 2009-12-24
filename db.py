from pymongo.connection import Connection
from kouyou.models import Board, Post

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
    return self.get_board(board_code).count

  def get_board_id(self, board_code):
    board = self.boards.find_one({'board_code': board_code})
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

  def get_post(self, post_id):
    return Post(self.posts.find_one({'id': post_id}))

  def get_posts(self, boardid):
    latest_posts = list(self.posts.find({
      'board': boardid, 
    }))
    posts = [Post(post) for post in latest_posts]
    return posts

  def insert_post(self, post, thread_id=None):
    if not post.is_valid():
      return None
    id = self.increase_post_count(board_code)
    post.id = id
    if thread_id != None:
      # reply
      self.posts.update(
        {'id': thread_id}, 
        {'$push': {'replies': post.as_dict()}})
    else:
      self.posts.insert(post.as_dict())
    return id






