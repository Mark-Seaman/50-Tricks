#!/usr/bin/env python
# JSON with python

from  json import dumps,loads

x = dumps ({ 'user':'User Name', 'password':'Password' })
print x

y = loads(x)
print y
print 'User = %s' % y['user']
