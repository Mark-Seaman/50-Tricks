# Django settings for app project.

from os.path import abspath,dirname,join

DEBUG=True

# App startup
SECRET_KEY = 's!qs5!9(bhkv7#hn#172zm_*l#m)j(8lv1gj)#84p$9+^&amp;bn9e'
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
ROOT_DIR  = dirname(abspath(__file__))


# Static server
STATIC_ROOT = ''
STATIC_URL = '/static/'
