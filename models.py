
class Model(object):
  def __init__(self, d):
    if type(d) == type({}):
      for k in d.keys():
        self.__dict__[k] = d[k]

class Board(Model):
  @property
  def fullname(self):
    return ''.join(['/', self.board_code, '/ ', self.name])

