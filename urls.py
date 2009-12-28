from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^$', "kouyou.boards.views.index"),
    (r'^(\w+)$', 'kouyou.boards.views.board'),
    (r'^(\w+)/(\d+)$', 'kouyou.boards.views.board'),
    (r'^(\w+)/(\w+)$', 'kouyou.boards.views.thread'),
    (r'^(\w+)/(\w+)/(\d+)$', 'kouyou.boards.views.thread'),
)
