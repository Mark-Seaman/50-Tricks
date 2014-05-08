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

# List the minutes
def minutes(t):
    return to_time(t).minute + to_time(t).hour*60

# Sum up a list of individual times
def sum_time(time_list):
    total = 0
    for t in time_list:
        total += minutes(t)
        #print t, "%d:%d"%(total/60, total%60)
    return total

def print_total(total):
    print "    Total time:  %d:%d"%(total/60, total%60)
    print "    Total hours: %4.2f"%(total/60.0)
    print "    Rate:        $75/hour"
    print "    Amount due:  $%4.2f"%(total/60.0*75)

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
def get_work_time(t):
    return work_time(t[3],t[4],t[5],t[6])

# Print the difference in time for two sessions
def print_work_time(parts):
    print "%s,%s,%s"%(parts[1], parts[2], get_work_time(parts))

# Print out each day and the time worked
def print_time_sheet(days):
    time_list = []
    for day in days:    
        parts = day.split (', ')
        if len(parts)==7:
            print_work_time (parts)
            time_list.append(get_work_time(parts))
        else:
            print "**", day
    print_total(sum_time(time_list))
  
'''  
Oct 16 - Oct 31    
S, 10-16, get accounting data to Mike, 7:00, 8:30, 1:00, 1:00
M, 10-18, improve checkup system, 7:30, 12:00, 12:20, 6:00
T, 10-19, solved automation issue with system checkup, 8:00, 10:30, 11:30, 5:00
W, 10-20, documented troubleshooting tools, 8:00, 12:00, 12:15, 5:00
Th, 10-21, instructions for flash card replacements, 7:45, 12:00, 12:20, 4:00
M, 10-25, features for accounting and diagnostics, 7:30, 12:00, 12:20, 5:00
T, 10-26, enable automatic notifications, 8:00, 12:00, 12:10, 5:00
W, 10-27, integrity checker for accounting data, 8:00, 12:00, 12:20, 5:00
Th, 10-28, start on health monitor; checkup features, 8:00, 12:00, 12:10, 2:40
'''

timesheet = '''
M, 11-1, Implement basic data recorder, 8:00, 12:00, 12:30, 5:00
T, 11-2, Implement pressure and vend monitors, 8:00, 12:00, 1:00, 5:00
W, 11-3, Display vend count history in Support Center, 8:00, 11:15, 1:30, 5:30
Th, 11-4, Started backups to Frederick server, 8:00, 12:00, 1:00, 5:00
M, 11-8, Create Watermill pressure log, 8:00, 12:00, 12:20, 5:00
T, 11-9, Display the pressure log in Support Center, 8:00, 12:00, 12:20, 5:00
W, 11-10, Start on water production, 8:00, 11:40, 12:00, 5:00
Th, 11-11, Build and test 5.6, 8:10, 12:00, 12:40, 5:00
F, 11-12, Help with testing on 5.6, 8:00, 9:30, 9:30, 9:30
'''

print_time_sheet(timesheet.split ("\n"))

