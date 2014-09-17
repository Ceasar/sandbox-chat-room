from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'chatroom.views.index', name='index'),
    url(r'^messages$', 'chatroom.views.message', name='message'),
    url(r'^admin/', include(admin.site.urls)),
)
