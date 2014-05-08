#!/usr/bin/python
# Variable communication trick

from varCom import *
from states import *

#-----------------------------------------------------------------------------
# Drinker State machine

drinker_states = '''
drinking,requesting,done
requesting,drinking,got_one
'''

# Drinking
def drinker_drinking():
    print 'Drinker: Drink beer'
    trigger(drinker_done)

# Requesting
def drinker_requesting():
    print 'Drinker: More beer'
    trigger(bar_keep_request)

# Actions that can be called from the state machine
def drinker_state(state):         
    if debug: print 'Entering', state
    if state == 'drinking':     drinker_drinking()
    if state == 'requesting':   drinker_requesting()

# Process one event
def drinker_event(event):
    global dstate 
    if debug: print 'Drinker event: ', event
    dstate = run_one_step(drinker, dstate, event,  drinker_state)

def drinker_run():
    if debug: print 'Drinker state:', dstate
    if triggered(drinker_has_beer): drinker_event('got_one')
    if triggered(drinker_done):     drinker_event('done')

#-----------------------------------------------------------------------------
# Application Variables

drinker   = create_machine(drinker_states)
dstate    = 'requesting'
