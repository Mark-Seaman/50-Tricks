#!/usr/bin/python
# Build a minimalistic state machine in python

debug = False

#----------------------------------------------------------------------------------------
# State machine domain

# Advance the state machine based on the event
def transition(state, event):
    if debug: print state
    key=state+'/'+event
    if debug: print 'Key:',key
    if (state_machine.has_key(key)):
        if debug: print '[Key]:',state_machine[key]
        (action,state) = state_machine[key]
        action()
        return state
    return state

# Verify a single state transition
def test_transition (state, event, new_state):
    if debug: print 'transistion:', state,'+', event,'-->', new_state
    x = transition (state, event)
    if debug: print 'state: ', "%-15s"%x
    assert (x == new_state)
    return x

# Create edges in graph
def add_transition(old_state, new_state, event, action):
    state_machine[old_state+'/'+event] = (action,new_state)

#----------------------------------------------------------------------------------------
# Problem domain

# Actions that can be called from the state machine
def set_timer():     
    if debug: print 'Action: set_timer'
def none():         
    if debug: print 'Action: none'
def send_set():    
    if debug: print 'Action: send_set'
def send_clear():   
    if debug: print 'Action: send_clear'

# States
s_clear   = 'state_clear'
s_sprob   = 'state_set_prob'
s_set     = 'state_set'
s_cprob   = 'state_clear_prob'

# Events
e_set     = 'set'
e_clear   = 'clear'
e_timeout = 'timeout'

# States/transitions/actions
state_machine = { }
add_transition(s_clear,   s_sprob,    e_set,      set_timer)
add_transition(s_sprob,   s_clear,    e_clear,    none)
add_transition(s_sprob,   s_set,      e_timeout,  send_set)
add_transition(s_set,     s_cprob,    e_clear,    set_timer)
add_transition(s_cprob,   s_set,      e_set,      none)
add_transition(s_cprob,   s_clear,    e_timeout,  send_clear)

# Test the edges in the state machine
def test_state_machine():
    state = s_clear
    state = test_transition (state, e_set,      s_sprob)
    state = test_transition (state, e_clear,    s_clear)
    state = test_transition (state, e_timeout,  s_clear)
    state = test_transition (state, e_set,      s_sprob)
    state = test_transition (state, e_timeout,  s_set)
    state = test_transition (state, e_clear,    s_cprob)
    state = test_transition (state, e_timeout,  s_clear)
    state = test_transition (state, e_set,      s_sprob)
 
test_state_machine()
