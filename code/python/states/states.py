#!/usr/bin/python
# Build a minimalistic state machine in python

debug = False
state = ''
state_machine = { }

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
    print 'you are now in ', state
    if (x != new_state): 
        print 'Connection problem: no path', event, 'from', x, 'to', new_state
    return x

# Create edges in graph
def add_transition(old_state, new_state, event, action):
    state_machine[old_state+'/'+event] = (action,new_state)

# Add a pair of transitions
def add_connection (node1, node2, edge1, edge2, action):
    add_transition(node1, node2, edge1, action)
    add_transition(node2, node1, edge2, action)

# Do a sequence of events and return the final state
def run_sequence(state, events):
    for step in events:
        state = transition (state, step)
        print 'you are now in ', state
    return state
