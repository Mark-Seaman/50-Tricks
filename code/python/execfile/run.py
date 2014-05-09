#!/usr/bin/python
# Run an app using system

from os import system

print 'Control is given away, and app blocks'

# This script blocks until gedit exits
system('gedit')

print 'Gedit has exited'
