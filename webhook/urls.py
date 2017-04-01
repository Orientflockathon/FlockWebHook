from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webhook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^check$', 'orient.views.check', name='check'),
    url(r'^listenEvent$', 'orient.views.listenEvent', name='listenEvent'),
    url(r'^linkedin/$', 'api.views.index', name='home'),
)
