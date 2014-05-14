#!/usr/bin/python
# This command intepeter runs a new process for each command line given.  It terminates when
# it sees the done signal.  Each command creates a new process and the output is captured and 
# processed by the worker.

import sys
import subprocess
import time

# Execute the command and copy command output to the pipe
def execute_cmd(input, output):
    p=subprocess.Popen(input[:-1], shell=True, stdout=subprocess.PIPE)
    for line in p.stdout.readlines():
        output.write(line)


# Start a new process, and capture its output, and echo the results
def output_results(input, output):
    sys.stdout.write("Running "+input)
    execute_cmd(input, output)
    sys.stdout.write("Done with "+input)
    sys.stdout.write("-----------------------------------------------------------\n")
    output.write("done\n")
    output.flush()


# This is a process that listens to the input and executes the commands.
while True:

    # Read a single command line
    input = sys.stdin.readline()
    
    # Interpreter terminates when it sees a 'done' command.
    if (input == "done\n"):
        sys.stdout.write("done\n")
        break

    # Spawn a worker and wait for it to end
    output_results(input, sys.stdout)
