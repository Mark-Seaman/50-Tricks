#!/usr/bin/python
# Variable communication trick

from states import *

#-----------------------------------------------------------------------------
# State machine

# Actions that can be called from the state machine
def enter_room(room):         
    print 'Entering', labels[room]


# States
labels = {
    'drive': 'the driveway',
    'porch': 'the porch',
    'lake': 'the lake',
    'entry': 'the entry way',
    'deck': 'the deck',
    'garage': 'the garage',
    'office': 'the office',
    'bed': 'master bedroom',
    'bath1': 'the guest bathroom',
    'bath2': 'the master bathroom',
    'hall': 'main hallway',
    'basement': 'the basement',
    'family': 'the family room',
    'dining': 'the dining area',
    'kitchen': 'the kitchen',
    'nook': 'the breakfast nook',
}

# Events
n  = 'n'
s  = 's'
e  = 'e'
w  = 'w'
we = 'we'
ew = 'ew'
ns = 'ns'
sn = 'sn'


# Connections
connections = []

connect = '''
drive,porch,we
drive,garage,sn
porch,entry,we
entry,office,ns
entry,bed,sn
entry,hall,we
hall,dining,we
hall,basement,sn
hall,bath1,ns
dining,deck,we
deck,lake,we
'''

create_double_connections(connect)

# walk a particular path
state = 'drive'
events = (s, n, w, w, w, w, w, w, e, e, e, e, e, e,)
run_sequence(state, events, enter_room)
