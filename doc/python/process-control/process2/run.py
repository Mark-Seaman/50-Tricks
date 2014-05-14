#!/usr/bin/python

import sys
import subprocess
import time

# Run the interpreter process and control STDIN and STDOUT 
interpreter=subprocess.Popen(['interpreter.py'], shell=False,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Print the results of the command
def output_results():
    while True:
        output = interpreter.stdout.readline()
        if (output == "done\n"):
            break
        print output[:-1]

# Send the command to the interpreter and process the output
def run_script(cmd):
    interpreter.stdin.write('%s\n' % cmd)
    output_results()

# Add sleep to see timing of output.
for cmd in ['ls','df','done']:
    run_script(cmd)
    time.sleep(1)


