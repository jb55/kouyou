from datetime import datetime
from django import forms
from django.http import HttpResponseRedirect
from kouyou.boards.models import Post
from kouyou.boards.db import BoardManager

class ReplyForm(forms.Form):
  author = forms.CharField(max_length=128, required=False)
  tripcode = forms.CharField(max_length=128, required=False,
    widget=forms.PasswordInput(render_value=False))
  msg = forms.CharField(widget=forms.widgets.Textarea(), max_length=65536)
  image = forms.FileField(required=False)
  audio = forms.FileField(required=False)

class NewThreadForm(ReplyForm):
  topic = forms.CharField(max_length=128, required=False)

def post_from_form(form):
  attrs = ('author', 'topic', 'tripcode', 'msg', 'image', 'audio')
  post = Post()
  # go through all the form attributes, pick out
  # the ones that exist and insert them into the
  # post object
  for attr in attrs:
    if form.cleaned_data.has_key(attr):
      data = form.cleaned_data[attr]
      setattr(post, attr, data)
  return post 

def do_post(req, board_code, thread_id=None):
  post = Post()
  form = None
  if thread_id:
    form = ReplyForm(req.POST)
  else:
    form = NewThreadForm(req.POST)

  if form.is_valid():
    bm = BoardManager()
    post = post_from_form(form)
    bm.insert_post(post, board_code, thread_id)

  if thread_id:
    return HttpResponseRedirect(''.join(['/', board_code, '/', thread_id]))
  else:
    return HttpResponseRedirect('/' + board_code)

