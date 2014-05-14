#!/usr/bin/python

import sys

# This is a process that listens to the input and echos to the output.
# It terminates when it sees 'done'.
while True:
    input = sys.stdin.readline()
    sys.stdout.write("worker echo "+input)
    if (input == "done\n"):
        break
    sys.stdout.flush()

