#!/usr/bin/python
# Calculate odds of success for hashing

# Number of variables
n = 10.

# Number of slots
m = 1000.

# Calculate the odds of avoiding collisions
def probability_of_success(n,m):
    return (1 - n/m)**n * 100

def fifty_fifty(n):
    return n / (1 - .5**(1/n))

def assess(n,m):
    print 'Probabilty of success = %f%%, for %d vars in %d space'%(probability_of_success(n,m), n, m)
    print '50%% size(%d) = %d\n'%(n, fifty_fifty(n))

# Pack 10 vars into 100 slots
assess(10.,100.)

# Pack 10 vars into 200 slots
assess(10.,200.)

# Pack 1000 vars into 100,000 slots
assess(1000.,100000.)

# Pack 5K vars into 1M slots
assess(5000.,10000000.)


print '''
Consider computing a table of indexes into memory.
Create a table with 1M slots of two bytes.
Each slot points to one of 5000 vars in shared memory.
Each attempt at the layout will have an 8% chance of success if fully random. 
'''
