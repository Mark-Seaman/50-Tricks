#!/usr/bin/python

#Python 2.6 
from datetime import strftime,localtime, strptime, ctime, time, mktime

# Convert from string to seconds after 1970
def to_time(s):
     return mktime(strptime(s, "%H:%M"))
 
# Format the elapsed time
def elapsed(t):
    if t>0:
        return "%d:%02d"%(int(t/3600),t%3600/60)
    else:
        return "%d:%02d"%(int(t/3600),60-t%3600/60)

# Subtract two time strings
def time_diff(t1,t2):
     return elapsed(to_time(t2)-to_time(t1))

# Subtract two time strings
def work_time(t1,t2,t3,t4):
     return elapsed(to_time(t2 )- to_time(t1) + to_time(t4) - to_time(t3))

# Convert from a time record to string
def time_str(t):
     return strftime("%H:%M", t)

def do_test():
    print "Time since 12:00", time_diff('12:00', time_str(localtime()))
    print "Time since 5:00",  time_diff('19:00', time_str(localtime()))
    print time_diff ('3:00','5:00')
    print time_diff ('8:00','17:00')
    print work_time('8:00','12:00','1:00','5:00')
#do_test()

# Print the difference in time for two sessions
def print_work_time(s):
    t = s.split (', ')
    print t
    print work_time(t[2],t[3],t[4],t[5])

print_work_time ("M, 10-4, 8:00, 12:00, 12:40, 17:00")
print_work_time ("M, 10-4, 8:00, 12:00, 12:40, 5:00")
print_work_time ("T, 10-5, 7:00, 11:00, 11:15, 4:15")
print_work_time ("W, 10-6, 7:00, 11:30, 1:30, 5:00")
print_work_time ("Th, 10-7, 8:00, 12:00, 12:20, 5:00")
print_work_time ("F, 10-8, 8:00, 11:00, 1:00, 1:00")
print_work_time ("M, 10-11, 7:00, 10:00, 12:30, 5:00")

