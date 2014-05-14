#!/usr/bin/python
# Variable communication trick

from states import *

#-----------------------------------------------------------------------------
# Application Variables

bottles_on_wall = 100

#-----------------------------------------------------------------------------
# State Handlers

# Bar Keep
def bar_keep_take_one_down():
    global bottles_on_wall
    if bottles_on_wall>0:
        print 'Take one down, pass it around'
        bottles_on_wall -= 1
        print '%d bottles on wall'% bottles_on_wall

def bar_keep_idle():
    print 'Waiting'

def bar_keep_pass_it():
    print 'Take this one'

#-----------------------------------------------------------------------------
# State machine

# Actions that can be called from the state machine
def bar_keep_state(state):         
    if state == 'idle':           bar_keep_idle()
    if state == 'take_one_down':  bar_keep_take_one_down()
    if state == 'pass_it_around': bar_keep_pass_it()

bar_keep_states = '''
idle,take_one_down,request
take_one_down,pass_it_around,got_one
pass_it_around,idle,passed_bottle
'''

bar_keep  = create_machine(bar_keep_states)

# walk a particular path
state = 'idle'

events = ( 'request',  'request', 'request','got_one')
state = run_sequence(bar_keep, state, events, bar_keep_state)

events = ( 'passed_bottle',  'passed_bottle', 'request', 'got_one')
state = run_sequence(bar_keep, state, events, bar_keep_state)
