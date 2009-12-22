#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from waka import make_app

sock_path = '/tmp/waka-fcgi.sock'

application = make_app()
WSGIServer(application, bindAddress=sock_path).run()
