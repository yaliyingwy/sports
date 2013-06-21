from django.conf.urls import *


urlpatterns = patterns(('ksports.views'),
        url(r'^$', 'getPersons', name='sports'),
        url(r'^add/$', 'addPerson', name='add'),
        url(r'^about/$', 'about', name='about'),
        )
