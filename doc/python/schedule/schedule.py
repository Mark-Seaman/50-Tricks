#!/usr/bin/python
# Run a scheduler for long running tasks

from os   import system
from time import sleep


# Run this once each hour
def run_hourly(command):
    print 'Running ...',command
    system ('nohup '+command+' 2>&1 > /tmp/schedule.out &')

# Run the hourly command 24 times
def run_schedule():
    for h in range(24):
        run_hourly('echo hourly-linux-task %d'%h)
        sleep (60*60)  # 60 seconds * 60 minutes

# Bash usage:  schedule.py &> /dev/null
run_schedule()
