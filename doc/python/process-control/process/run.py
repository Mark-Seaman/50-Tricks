#!/usr/bin/python

import sys
import subprocess
import time

# Run the above process and control STDIN and STDOUT 
p=subprocess.Popen(['process.py'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Send two input lines and then done.
# Add sleep to see timing of output.
for cmd in ('ls','df','done'):
    p.stdin.write('%s\n' % cmd)
    output = p.stdout.readline()
    print output[:-1]
    time.sleep(1)


