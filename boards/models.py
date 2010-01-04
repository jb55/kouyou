from datetime import datetime

class Model(object):
  def __init__(self, d={}):
    if type(d) == type({}):
      for k in d.keys():
        setattr(self, k, d[k])

  @property
  def oid(self):
    return self._id;

  def as_dict(self):
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
          'dead',
          'sage',
          'topic',
          'bumped_at',
          'tripcode',
          'created_at',
          'board',
          'replies',
          'msg',)

  bump_fields = ['dead', 'sage']

  @staticmethod
  def new_post(dict):
    post = Post(dict)
    post.created_at = datetime.utcnow()
    return post

  def is_valid(self):
    return True

  def can_bump(self):
    for field in Post.bump_fields:
      if hasattr(self, field):
        return False
    return True
