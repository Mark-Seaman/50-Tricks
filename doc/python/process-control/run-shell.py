#!/usr/bin/python

from subprocess import  Popen,PIPE

# Run the sh as a process and send commands as STDIN
def do_command(command):
    p = Popen(['ssh','wmexpress@wmexpress.webfactional.com'], shell=False, stdin=PIPE, stdout=PIPE)
    return p.communicate(command)[0]

# Execute commands on the remote machine
print do_command('ls\necho Hello There\nhostname')


