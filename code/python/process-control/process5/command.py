#!/usr/bin/python

import sys
import subprocess
import time

# Run the command and send the output to STDOUT 
def run_command(cmd, output):
    p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in p.stdout.readlines():
        output.write(line)
    output.flush()

# This is a process that listens to the input and echos to the output.
# It terminates when it sees 'done'.
while True:
    input = sys.stdin.readline()
    sys.stdout.write("Running "+input)
    if (input == "done\n"):
        break
    #run_command(input[:-1], sys.stdout)
    p=subprocess.Popen(input[:-1], shell=True, stdout=subprocess.PIPE)
    for line in p.stdout.readlines():
        sys.stdout.write(line)
    sys.stdout.flush()

