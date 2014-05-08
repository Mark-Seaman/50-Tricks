#!/usr/bin/python
# Generate a bunch of output to simulate a real task

import sys
import time

print 'Bogus chromosome data: CHROMOSOME ', sys.argv[1]
time.sleep(30)
for line in range(100):
     for x in range(100):  print '%02d'%x,
     print line
