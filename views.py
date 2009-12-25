from glashammer.utils import render_response
from kouyou.db import BoardManager
from kouyou.forms import NewThreadForm, ReplyForm

def board(req, board_code):
  bm = BoardManager()
  board = bm.get_board(board_code)

  data = {}
  data["board"] = board
  data["posts"] = bm.get_posts(board.board_id)
  data["form"] = NewThreadForm()
  return render_response('board.htm', **data)
  
def index(req):
  data = {}
  return render_response('index.htm', **data)

def thread(req, board_code, thread_id):
  bm = BoardManager()
  board = bm.get_board(board_code)

  data = {}
  data["board"] = board
  post = bm.get_thread(thread_id)
  data["posts"] = (post,)
  data["form"] = ReplyForm()

  return render_response('thread.htm', **data)
