from django.shortcuts import render_to_response
from kouyou.boards.db import BoardManager, NUM_PAGES
from kouyou.boards.forms import NewThreadForm, ReplyForm

def board(req, board_code, page=1):
  bm = BoardManager()
  board = bm.get_board(board_code)
  page = int(page)

  data = {}
  data["boards"] = bm.get_boards()
  data["board"] = board
  data["posts"] = bm.get_posts(board.board_id, page)
  data["pages"] = xrange(1, NUM_PAGES + 1)
  data["form"] = NewThreadForm()
  return render_to_response('board.htm', data)
  
def index(req):
  data = {}
  return render_to_response('index.htm', data)

def thread(req, board_code, thread_id):
  bm = BoardManager()
  board = bm.get_board(board_code)

  data = {}
  data["boards"] = bm.get_boards()
  data["board"] = board
  post = bm.get_thread(thread_id)
  data["posts"] = (post,)
  data["thread"] = post
  data["form"] = ReplyForm()

  return render_to_response('thread.htm', data)
