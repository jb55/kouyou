from django.conf.urls.defaults import *

board_match = r'(\w{1,3})'
thread_match = r'(\w{24})'
board_thread = (board_match, thread_match)

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^$', "kouyou.boards.views.index"),
    (r'^%s$' % board_match, 'kouyou.boards.views.board'),
    (r'^%s/newpost$' % board_match, 'kouyou.boards.forms.do_post'),
    (r'^%s/(\d+)$' % board_match, 'kouyou.boards.views.board'),
    (r'^%s/%s$' % board_thread, 'kouyou.boards.views.thread'),
    (r'^%s/%s$' % board_thread, 'kouyou.boards.views.thread'),
    (r'^%s/%s/reply$' % board_thread, 'kouyou.boards.forms.do_post'),
    (r'^%s/%s/(\d+)$' % board_thread, 'kouyou.boards.views.thread'),
)
