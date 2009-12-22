#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from kouyou.app import make_app

sock_path = '/tmp/kouyou-fcgi.sock'

application = make_app()
WSGIServer(application, bindAddress=sock_path).run()
