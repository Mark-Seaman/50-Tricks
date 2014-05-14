#!/usr/bin/python
# Build a minimalistic state machine in python

from states import *

# Actions that can be called from the state machine
def enter_room():         
    pass


# States
drive   = 'the driveway'
porch   = 'the porch'
lake    = 'the lake'
entry   = 'the entry way'
deck    = 'the deck'
garage  = 'the garage'
office  = 'the office'
bed     = 'master bedroom'
bath1   = 'the guest bathroom'
bath2   = 'the master bathroom'
hall    = 'main hallway'
basement= 'the basement'
family  = 'the family room'
dining  = 'the dining area'
kitchen = 'the kitchen'
nook    = 'the breakfast nook'

# Events
n  = 'n'
s  = 's'
e  = 'e'
w  = 'w'
we = 'we'
ew = 'ew'
ns = 'ns'
sn = 'sn'

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

# Connections
connections = [
        [drive,   porch,    we ],
        [drive,   garage,   sn ],
        [porch,   entry,    we ],
        [entry,   office,   ns ],
        [entry,   bed,      sn ],
        [entry,   hall,     we ],
        [hall,    dining,   we ],
        [hall,    basement, sn ],
        [hall,    bath1,    ns ],
        [dining,  deck,     we ],
        [deck,    lake,     we ],
        ]

# States/transitions/actions
#for c in connections:
#    add_connection (c[0], c[1], c[2][0], c[2][1], enter_room)

for c in connect.split('\n')[1:-1]:
    s = c.split(',')
    add_connection (s[0], s[1], s[2][0], s[2][1], enter_room)


# Test the edges in the state machine
def test_state_machine():
    global state
    path = (
        (s, garage), 
        (n, drive), 
        (w, porch), 
        (w, entry), 
        (n, office),
        (s, entry),
        (s, bed),
        (n, entry),
        (w, hall), 
        (s, basement),
        (n, hall),
        (n, bath1),
        (s, hall),
        (w, dining), 
        (w, deck), 
        (w, lake),
        (e, deck),
        (e, dining), 
        (e, hall), 
        (e, entry),
        (e, porch), 
        (e, drive), 
        )
    for step in path:
        state = test_transition (state, step[0],  step[1])
   
# Run the map in test mode
state = drive
test_state_machine()

# walk a particular path
path = (s, n, w, w, w, w, w, w, e, e, e, e, e, e,)
run_sequence(state,path)
