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
drinker   = create_machine(drinker_states)
dstate    = 'requesting'


# Actions that can be called from the state machine
def enter_state(state):         
    if state == 'drinking':     drinking()
    if state == 'requesting':   requesting()

# Process one event
def do_event(event):
    global dstate 
    dstate = run_one_step (drinker, dstate, event,  enter_state)

def drinker_run():
    if triggered(drinker_has_beer): do_event('got_one')
    if triggered(drinker_done):     do_event('done')

#-----------------------------------------------------------------------------
# Drinker State handlers

# Drinking
def drinking():
    print 'Drinker: Drink beer'
    trigger(drinker_done)

# Requesting
def requesting():
    print 'Drinker: More beer'
    trigger(bar_keep_request)

