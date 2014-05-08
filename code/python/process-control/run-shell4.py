#!/usr/bin/python

import sys
import subprocess
import time

# Run the sh as a process and send commands as STDIN
p=subprocess.Popen('sh',stdin=subprocess.PIPE)

# Execute one command
p.stdin.write("ls\n")

time.sleep (3)

# Execute one command
p.stdin.write("ls -l\n")

time.sleep (3)

# Execute one command
p.stdin.write("hostname\n")
p.stdin.close()


