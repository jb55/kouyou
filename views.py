from glashammer.utils import render_response
from kouyou.db import BoardManager, PostManager

def board(req, board_code):
  pm = PostManager()
  bm = BoardManager()
  board = bm.get_board(board_code)

  data = {}
  data["name"] = "Bill"
  data["board"] = board
  data["posts"] = pm.get_posts(board.board_id)
  return render_response('board.htm', **data)
  
def index(req):
  data = {}
  return render_response('index.htm', **data)
