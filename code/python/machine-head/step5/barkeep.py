#!/usr/bin/python
# Variable communication trick

from varCom import *
from states  import *
from drinker import *

#-----------------------------------------------------------------------------
# Bar Keep State machine

bar_keep_states = '''
idle,take_one_down,request
take_one_down,pass_it_around,got_one
pass_it_around,idle,passed_bottle
'''

# Idle
def bar_keep_idle():
    print 'Bar Keep: Waiting'

# Take one down
def bar_keep_take_one_down():
    bottles = getValue(bottles_on_wall)
    if getValue(bottles_on_wall)>0:
        print 'Bar Keep: Take one down, pass it around'
        bottles -= 1
        print 'Bar Keep: %d bottles on wall'% bottles
        setValue(bottles_on_wall, bottles)
        trigger(bar_keep_got_one)

# Pass it around
def bar_keep_pass_it():
    print 'Bar Keep: Take this one'
    trigger(bar_keep_passed_bottle)
    trigger(drinker_has_beer)
 
# Actions that can be called from the state machine
def bar_keep_state(state):         
    if debug: print 'Entering', state
    if state == 'idle':           bar_keep_idle()
    if state == 'take_one_down':  bar_keep_take_one_down()
    if state == 'pass_it_around': bar_keep_pass_it()

# Process one event
def bar_keep_event(event):
    global bstate 
    if debug: print 'Bar keep event: ', bstate, event
    bstate = run_one_step(bar_keep, bstate, event,  bar_keep_state)

# Capture inputs
def bar_keep_run():
    if debug: print 'Bar Keep state:', bstate
    if triggered(bar_keep_request):       bar_keep_event('request')
    if triggered(bar_keep_got_one):       bar_keep_event('got_one')
    if triggered(bar_keep_passed_bottle): bar_keep_event('passed_bottle')

#-----------------------------------------------------------------------------
# Application Variables

bottles_on_wall = init(100)


bar_keep  = create_machine(bar_keep_states)
bstate = 'idle'
