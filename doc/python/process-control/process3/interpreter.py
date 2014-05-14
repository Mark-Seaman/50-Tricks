#!/usr/bin/python

import sys
import subprocess
import time


#Display the results from executing a shell script
def output_results(cmd_text, output):

    p.stdin.write("%s\n" % cmd_text)
    p=subprocess.Popen(cmd_text[:-1], shell=True, stdout=subprocess.PIPE)
    #p=subprocess.Popen(cmd_text[:-1], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    for line in p.stdout.readlines():
        output.write(line)

    #sys.stdout.write("-----------------------------------------------------------\n")
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

