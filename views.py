from glashammer.utils import render_response
from kouyou.db import BoardManager

def board(req, board_code):
  data = {}
  data["name"] = "Bill"
  data["board"] = BoardManager().get_board(board_code)
  return render_response('board.htm', **data)
  
def index(req):
  data = {}
  return render_response('index.htm', **data)
