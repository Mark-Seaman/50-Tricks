#!/usr/bin/python

import sys
import subprocess
import time

# Run the sh as a process and send commands as STDIN
process=subprocess.Popen('sh', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Execute one command
process.stdin.write("ls\n")
process.stdin.flush()

time.sleep (3)

# Execute one command
process.stdin.write("ls -l\n")
process.stdin.flush()

time.sleep (3)

# Execute one command
process.stdin.write("hostname\n")
process.stdin.close()

# Read the output
print process.stdout.read()

