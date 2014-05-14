#!/usr/bin/python
# Variable communication trick

from varCom import *
from states import *

#-----------------------------------------------------------------------------
# Application Variables

bottles_on_wall = init(100)
has_beer        = init(True)

#-----------------------------------------------------------------------------
# Bar Keep State machine

bar_keep_states = '''
idle,take_one_down,request
take_one_down,pass_it_around,got_one
pass_it_around,idle,passed_bottle
'''

# Take one down
def bar_keep_take_one_down():
    bottles = getValue(bottles_on_wall)
    if getValue(bottles_on_wall)>0:
        print 'Take one down, pass it around'
        bottles -= 1
        print '%d bottles on wall'% bottles
        setValue(bottles_on_wall, bottles)
        setValue(has_beer,True)

# Idle
def bar_keep_idle():
    print 'Waiting'

# Pass it around
def bar_keep_pass_it():
    print 'Take this one'

# Actions that can be called from the state machine
def bar_keep_state(state):         
    if debug: print 'Entering', state
    if state == 'idle':           bar_keep_idle()
    if state == 'take_one_down':  bar_keep_take_one_down()
    if state == 'pass_it_around': bar_keep_pass_it()

#-----------------------------------------------------------------------------
# Drinker State machine

drinker_states = '''
drinking,requesting,done
requesting,drinking,got_one
'''

# Drinking
def drinker_drinking():
    if getValue(has_beer):
        print 'Drink beer'
        setValue(has_beer,False)

# Requesting
def drinker_requesting():
    print 'More beer'

# Actions that can be called from the state machine
def drinker_state(state):         
    if debug: print 'Entering', state
    if state == 'drinking':     drinker_drinking()
    if state == 'requesting':   drinker_requesting()

#-----------------------------------------------------------------------------
# Run State machines

bar_keep  = create_machine(bar_keep_states)

# walk a particular path
bstate = 'idle'

events = ( 'request',  'request', 'request','got_one')
bstate = run_sequence(bar_keep, bstate, events, bar_keep_state)

bstate = run_one_step(state_machine, bstate, 'request',  bar_keep_state)

dstate = 'drinking'
drinker = create_machine(drinker_states)
events = ('got_one','got_one','done','done')
dstate = run_sequence(drinker, dstate, events, drinker_state)

events = ( 'passed_bottle',  'passed_bottle', 'request', 'got_one')
bstate = run_sequence(bar_keep, bstate, events, bar_keep_state)
