CONST_ANONYMOUS = "Anonymous"

class Model(object):
  def __init__(self, d):
    if type(d) == type({}):
      for k in d.keys():
        self.__dict__[k] = d[k]
    self.raw = d

class Board(Model):
  @property
  def fullname(self):
    return ''.join(['/', self.board_code, '/ ', self.name])

class Post(Model):
  def __init__(self, d):
    super(Post, self).__init__(d)
    if hasattr(self, "replies"):
      post_replies = [Post(reply) for reply in self.replies]
      self.replies = post_replies
    if not hasattr(self, "author"):
      self.author = CONST_ANONYMOUS
    else:
      if self.author == "" or self.author == None:
        self.author = CONST_ANONYMOUS
