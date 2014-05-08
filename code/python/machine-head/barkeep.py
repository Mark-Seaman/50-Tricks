#!/usr/bin/python
# Variable communication trick

from varCom import *
from states  import *

bottles_on_wall = init(100)

#-----------------------------------------------------------------------------
# Bar Keep State machine

bar_keep_states = '''
idle,take_one_down,request
take_one_down,pass_it_around,got_one
pass_it_around,idle,passed_bottle
'''

bar_keep  = create_machine(bar_keep_states)
bstate = 'idle'

# Actions that can be called from the state machine
def enter_state(state):         
    if state == 'idle':           bar_keep_idle()
    if state == 'take_one_down':  bar_keep_take_one_down()
    if state == 'pass_it_around': bar_keep_pass_it()

# Process one event
def do_event(event):
    global bstate 
    bstate = run_one_step(bar_keep, bstate, event,  enter_state)

# Capture inputs
def bar_keep_run():
    if triggered(bar_keep_request):       do_event('request')
    if triggered(bar_keep_got_one):       do_event('got_one')
    if triggered(bar_keep_passed_bottle): do_event('passed_bottle')

#-----------------------------------------------------------------------------
# Bar Keep action handlers

# Idle
def bar_keep_idle():
    print 'Bar Keep: Waiting for orders'

# Take one down and signal the others
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
