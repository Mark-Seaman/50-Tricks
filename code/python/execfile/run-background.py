#!/usr/bin/python
# Run an app using execfile

from os import execvp

print 'Pass control to gedit.'

# Control is given away
execvp('gedit', [ 'abc.txt' ])
print 'This app blocks until gedit closes.'

print 'This statement is never executed.   Control is taken by gedit.'
