#!/usr/bin/python
# Run an app using execfile

execfile('exec.py')

import os
# Control is given away
#os.execvp('gedit', [ 'abc.txt' ])

# This script blocks until gedit exits
os.system('gedit')
print 'Gedit has exited'
