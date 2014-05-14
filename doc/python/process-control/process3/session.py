#!/usr/bin/python

import sys
import subprocess
import time

# Create the interpreter the first time
interpreter = None

# Run the interpreter process and control STDIN and STDOUT 
def start_session(interpreter):
    if (interpreter == None):
        print 'new interpreter'
        return subprocess.Popen(['interpreter.py'], shell=False, 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    else:
        print 'old interpreter'
        return interpreter

# Print the results of the command
def output_results(interpreter):
    while True:
        output = interpreter.stdout.readline()
        print 'session output', output 
        if (output == "END_SESSION\n"):
            interpreter = None
            break
        if (output == "END_COMMAND\n"):
            break
        print output[:-1]

# Send the command to the interpreter and process the output
def run_command(interpreter, cmd):
    interpreter.stdin.write('%s' % cmd)
    output_results(interpreter)

# Terminate the session
def end_session(interpreter):
    run_command(interpreter, "END_SESSION\n")

# Send each command in the script to the interpreter
def run_script(interpreter, cmd):
    interpreter = start_session(interpreter)
    run_command(interpreter, cmd)
    end_session(interpreter)
    time.sleep(3)

# Read a script from a text file into a string
def read_script_file (script):
    lines = open(script, "r").readlines()
    return  "".join(lines)

# Execute the script by sending it to an interpreter
def execute_script(script_file):
    print 'execute_script', script_file
    run_script(interpreter, read_script_file (script_file))

