#!/usr/bin/python

import sys
import subprocess
import time

class Session:

    # Create the remote_shell the first time
    remote_shell = None

    def get (self):
        if (remote_shell == None):
            return subprocess.Popen(['remote_shell.py'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        else:
            return remote_shell

# Run the remote_shell process and control STDIN and STDOUT 
def start_session(remote_shell):
    return remote_shell.get()

# Print the results of the command
def output_results(remote_shell):
    while True:
        output = remote_shell.stdout.readline()
        if (output == "END_SESSION\n"):
            remote_shell = None
            break
        if (output == "END_COMMAND\n"):
            break
        print output[:-1]

# Send the command to the remote_shell and process the output
def run_command(remote_shell, cmd):
    remote_shell.stdin.write('%s' % cmd)
    output_results(remote_shell)

# Terminate the session
def end_session(remote_shell):
    run_command(remote_shell, "END_SESSION\n")

# Send each command in the script to the remote_shell
def run_script(cmd):
    remote_shell = start_session(remote_shell)
    run_command(remote_shell, cmd)
    end_session(remote_shell)

# Read a script from a text file into a string
def read_script_file (script):
    lines = open(script, "r").readlines()
    return  "".join(lines)

# Execute the script by sending it to an remote_shell
def execute_script(self,script_file):
    run_script(read_script_file (script_file))

