#!/usr/bin/python

def set_timer():    print 'Action: set_timer'
def none():         print 'Action: none'
def send_set():     print 'Action: send_set'
def send_clear():   print 'Action: send_clear'

state_machine = { 
    'clear/set':                (set_timer,    'set_probation'),
 
    'set_probation/clear':      (none,         'clear'),
    'set_probation/timeout':    (send_set,     'set'),

    'set/clear':                (set_timer,    'clear_probation'),

    'clear_probation/timeout':  (none,         'clear'),
    'clear_probation/clear':    (send_clear,   'clear'),
}

def new_state(state, event):
    key=state+'/'+event
    if (state_machine.has_key(key)):
        (action,state) = state_machine[key]
        action()
        #print 'state: ', "%-15s"%state
        return state
    return state

state = 'clear'
state = new_state (state, 'set')
assert (state=='set_probation')

state = new_state (state, 'clear')
assert (state=='clear')

state = new_state (state, 'timeout')
assert (state=='clear')

state = new_state (state, 'set')
assert (state=='set_probation')

state = new_state (state, 'timeout')
assert (state=='set')

state = new_state (state, 'clear')
assert (state=='clear_probation')

state = new_state (state, 'timeout')
assert (state=='clear')

state = new_state (state, 'set')
assert (state=='set_probation')

