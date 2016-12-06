import os
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^json/$', 'tagging_smartcomplete.views.json_tags', name='tagging-smartcomplete-json'),
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': os.path.abspath(os.path.dirname(__file__) + "/media")},
        name = 'tagging-smartcomplete-media'),
)
