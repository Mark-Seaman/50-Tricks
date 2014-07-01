from files import do_command


print map (lambda x:'RESULT'+x, do_command('ls -l').split('\n'))
