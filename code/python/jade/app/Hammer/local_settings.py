from platform import node

if 'seaman' not in node(): 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'simpleapps',
            'USER': 'simpleapps',
            'PASSWORD': 'JIL013sa',
            'HOST': '', 
            'PORT': '', 
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'hammer.db', 
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
            }
        }
