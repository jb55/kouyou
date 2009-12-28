from wtforms import (Form, TextField, 
  PasswordField, validators, FileField, TextAreaField)
from glashammer.utils import redirect
from datetime import datetime
from kouyou.boards.models import Post
from kouyou.boards.db import BoardManager

class ReplyForm(Form):
  author = TextField("Name", [validators.length(max=256)])
  tripcode = PasswordField("Tripcode", [validators.length(max=256)])
  msg = TextAreaField("Message")
  image = FileField("Image")
  audio = FileField("Audio")

class NewThreadForm(ReplyForm):
  topic = TextField("Topic", [validators.length(max=256)])

def post_from_form(form):
  attrs = ('author', 'topic', 'tripcode', 'msg', 'image', 'audio')
  post = Post()
  # go through all the form attributes, pick out
  # the ones that exist and insert them into the
  # post object
  for attr in attrs:
    if hasattr(form, attr):
      formattr = getattr(form, attr)
      if formattr.data:
        setattr(post, attr, formattr.data)
  return post 

def do_post(req, board_code, thread_id=None):
  post = Post()
  form = None
  if thread_id:
    form = ReplyForm(req.form)
  else:
    form = NewThreadForm(req.form)

  if form.validate():
    bm = BoardManager()
    post = post_from_form(form)
    bm.insert_post(post, board_code, thread_id)

  if thread_id:
    return redirect(''.join(['/', board_code, '/', thread_id]))
  else:
    return redirect('/' + board_code)
