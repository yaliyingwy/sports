from django.conf.urls import *


urlpatterns = patterns(('movie.views'),
        url(r'^$', 'listMovie', name='listMovie'),
        url(r'^(\d+)/$', 'showMovie', name='showMovie'),
        url(r'^login/$', 'login', name='login'),
        url(r'^logout/$', 'logout', name='logout'),
        url(r'^register/$', 'register', name='register'),
        )
