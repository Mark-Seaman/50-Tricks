#!/usr/bin/python

#Python 2.5
from datetime               import datetime, timedelta

#____________________________________________________
# Time
#____________________________________________________

# Convert from string to seconds after 1970
def to_time(s):
    return datetime.strptime(s, "%H:%M")

# Convert from a time record to string
def time_str(t):
     return t.strftime("%H:%M")

# Return time now as a string
def now_str():
    return time_str(datetime.now())  

# Format the elapsed time
def elapsed(t1,t2):
    if to_time(t2) >= to_time(t1):
        return str(to_time(t2)-to_time(t1))
    else:
        return "-"+str(to_time(t1)-to_time(t2))     
#____________________________________________________
# Work Time
#____________________________________________________

# Subtract two time strings
def work_time(t1,t2,t3,t4):
    td = to_time(t2)-to_time(t1)+to_time(t4)-to_time(t3)
    if td < timedelta(0):
        return str(td+timedelta(hours=12))[:-3]
    else:
        return str(td)[:-3]

# Test the time calculations
def do_test():
    print elapsed ('3:00','5:00')
    print elapsed ('10:00','9:00')
    print work_time('8:00','12:00','12:30','5:00')
#do_test()

# Print the difference in time for two sessions
def print_work_time(s):
    t = s.split (', ')
    #print t
    print "%-3s%-6s"%(t[0], t[1]), work_time(t[2],t[3],t[4],t[5])

# Print out each day and the time worked
def print_time_sheet(days):
    for day in days:
        print_work_time (day)

timesheet = '''
M, 10-4, setup Frederick backup system, 8:00, 12:00, 12:40, 5:00
T, 10-5, deploy 3020 & 3019, 7:00, 11:00, 11:15, 4:15
W, 10-6, build 5.5 code to fix bills, 7:00, 11:30, 1:30, 5:00
Th, 10-7, build checkup system, 8:00, 12:00, 12:20, 5:00
F, 10-8, move all logs to MillServer, 8:00, 11:00, 1:00, 1:00
M, 10-11, fix SSH keys; filter alert notifications, 7:00, 10:00, 12:30, 5:00
T, 10-12, accounting export, 7:00, 12:00, 3:00, 5:00
W, 10-13, create Watermill system logs, 7:30, 12:00, 12:30, 5:00
Th, 10-14, create sick list for watermills, 7:00, 12:00, 12:20, 4:30
'''

print_time_sheet( [ 'M, 10-4, setup Frederick backup system, 8:00, 12:00, 12:40, 5:00',
                    'T, 10-5, deploy 3020 & 3019, 7:00, 11:00, 11:15, 4:15' ] )
