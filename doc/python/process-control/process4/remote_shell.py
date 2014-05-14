#!/usr/bin/python

import sys
import subprocess
import time

# Create the remote shell
remote_shell = subprocess.Popen("sh", shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)


# This is a process that listens to the input and executes the commands.
while True:
    cmd = sys.stdin.readline()

    # Interpreter terminates when it sees a 'END_SESSION' command.
    if (cmd == "END_SESSION\n"):
        sys.stdout.write("END_SESSION\n")
        break

    # Execute the command
    remote_shell.stdin.write(cmd)

    # copy command output to the pipe
    for line in remote_shell.stdout.readlines():
        sys.stdout.write(line)

    sys.stdout.write("-----------------------------------------------------------\n")
    sys.stdout.write("END_COMMAND\n")
    sys.stdout.flush()

