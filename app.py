from glashammer.application import make_app as make_app_glas
from glashammer.utils import run_very_simple, Response, sibpath, local
from kouyou import views, forms
from kouyou.db import BoardManager

template_path = sibpath(__file__, 'templates')

def setup(app):
  app.add_template_searchpath(template_path)
  app.add_url('/', 'site/index')
  app.add_url('/<string(maxlength=3):board_code>', 'board/index')
  app.add_url('/<string(maxlength=3):board_code>/<int:page>', 'board/index')
  app.add_url('/<string(maxlength=3):board_code>/newpost', 'thread/new')
  app.add_url('/<string(maxlength=3):board_code>/<string:thread_id>',
              'thread/index')
  app.add_url('/<string(maxlength=3):board_code>/<string:thread_id>/reply',
              'thread/reply')
  app.add_view('thread/new', forms.do_post)
  app.add_view('thread/reply', forms.do_post)
  app.add_view('board/index', views.board)
  app.add_view('thread/index', views.thread)
  app.add_view('site/index', views.index)

  setup_template_globals(app)

def make_app():
  return make_app_glas(setup)

def setup_template_globals(app):
  bm = BoardManager()
  boards = bm.get_boards()
  app.add_template_global('boards', boards)

if __name__ == '__main__':
  make_app()
  run_very_simple(app)
