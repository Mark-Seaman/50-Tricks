#!/usr/bin/python

import sys
import subprocess
import time

# Execute the command and copy command output to the pipe
def execute_cmd(input, output):
    p=subprocess.Popen(input[:-1], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    for line in p.stdout.readlines():
        output.write(line)


#Display the results from executing a shell script
def output_results(cmd_text, output):
    execute_cmd(cmd_text, output)
    sys.stdout.write("-----------------------------------------------------------\n")
    output.write("END_COMMAND\n")
    output.flush()

# This is a process that listens to the input and executes the commands.
while True:
    input = sys.stdin.readline()

    # Interpreter terminates when it sees a 'END_SESSION' command.
    if (input == "END_SESSION\n"):
        sys.stdout.write("END_SESSION\n")
        break

    output_results(input, sys.stdout)

