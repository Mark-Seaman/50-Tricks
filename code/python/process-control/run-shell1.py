#!/usr/bin/python

from subprocess import Popen,PIPE

# Run the command as a process and capture stdout & print it
def do_command(cmd):
    return  Popen(cmd.split(),stdout=PIPE).stdout.read()

# Run the echo command
print do_command('echo Hello there')
