from datetime import datetime

CONST_ANONYMOUS = "Anonymous"

class Model(object):
  def __init__(self, d):
    if type(d) == type({}):
      for k in d.keys():
        setattr(self, k, d[k])

  def as_dict():
    d = {}
    for attr in self.attr:
      if hasattr(self, attr):
        d[attr] = getattr(self, attr)
    return d
        

class Board(Model):
  attr = ('_id',
          'count',
          'board_id',
          'board_code',
          'name',
          'modified_at') 

  @property
  def fullname(self):
    return ''.join(['/', self.board_code, '/ ', self.name])

class Post(Model):
  attr = ('_id',
          'id',
          'author',
          'topic',
          'tripcode',
          'created_at',
          'board',
          'replies',
          'msg',)

  @staticmethod
  def new_post(dict):
    post = Post(dict)
    post.created_at = datetime.utcnow()
    return post

  def is_valid(self):
    return True
