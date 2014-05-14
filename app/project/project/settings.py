# Django settings for app project.

from os.path import abspath,dirname,join

DEBUG=True


# App startup
SECRET_KEY = 's!qs5!9(bhkv7#hn#172zm_*l#m)j(8lv1gj)#84p$9+^&amp;bn9e'


# Location of router
ROOT_URLCONF = 'project.urls'


# Shim to run application from Apache
WSGI_APPLICATION = 'project.wsgi.application'


# Location of app directory
ROOT_DIR  = dirname(dirname(abspath(__file__)))


# Static server
STATIC_URL = '/static/'
STATIC_ROOT = ROOT_DIR+STATIC_URL


# Loading templates
TEMPLATE_DIRS = (
    ROOT_DIR+"/templates",
)
