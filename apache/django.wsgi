# -*- coding: utf-8 -*-

import os
import sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'sports.settings'
app_apth = "/home/ywen/sports"
sys.path.append(app_apth)
application = django.core.handlers.wsgi.WSGIHandler()
