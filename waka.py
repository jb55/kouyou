from glashammer.application import make_app as make_app_glas
from glashammer.utils import run_very_simple, Response

def hello_view(req):
  return Response('<h1>Hello World</h1>')

def setup(app):
  app.add_url('/', endpoint='hello/index', view=hello_view)

def make_app():
  return make_app_glas(setup)

if __name__ == '__main__':
  make_app()
  run_very_simple(app)
