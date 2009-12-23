from pymongo.connection import Connection
from kouyou.models import Board, Post

conn = Connection()
database = conn.kouyou

def get_database():
  return database

class PostManager():
  def __init__(self):
    self.posts = get_database().posts

  def get_posts(self, boardid):
    latest_posts = list(self.posts.find({
      'board': boardid, 
    }))
    posts = [Post(post) for post in latest_posts]
    return posts

class BoardManager():
  def __init__(self):
    self.boards = get_database().boards

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
