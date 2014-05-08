#!/usr/bin/python

from subprocess import Popen,PIPE
from time       import sleep

# Run the sh as a process and send commands as STDIN
p = Popen('sh', shell=True, stdin=PIPE)

# Execute one shell command
p.stdin.write("ls\n")
p.stdin.flush()

# Wait
sleep (3)

# Execute another command
p.stdin.write("ls -l\n")
p.stdin.flush()

# Wait
sleep (3)

# Execute another command
p.stdin.write("echo All Done")
p.stdin.flush()
