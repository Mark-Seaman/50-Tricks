#!/usr/bin/python
# Build a minimalistic state machine in python

debug = True
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
        state = state_machine[key]
        return state
    if debug: print 'transition:',state
    return state

# Verify a single state transition
def test_transition (state, event, new_state):
    if debug: print 'transistion:', state,'+', event,'-->', new_state
    x = transition (state, event)
    if debug: print 'you are now in ', state
    if (x != new_state): 
        print 'Connection problem: no path', event, 'from', x, 'to', new_state
    return x

# Create edges in graph
def add_transition(old_state, new_state, event):
    state_machine[old_state+'/'+event] = new_state

# Add a pair of transitions
def add_connection (node1, node2, edge1, edge2):
    add_transition(node1, node2, edge1)
    add_transition(node2, node1, edge2)


# Create all of the connectors to match the map
def create_machine(connect_map):
    for connector in connect_map.split('\n')[1:-1]:
        c = connector.split(',')
        if debug: print c
        if len(c)==3:
            if debug: print 'add_transition', c[0], c[1], c[2]
            add_transition (c[0], c[1], c[2])
    return state_machine

# Create all of the connectors to match the map
def create_double_connections(connect_map):
    for connector in connect_map.split('\n')[1:-1]:
        c = connector.split(',')
        if debug: print c
        if len(c)==3:
            if debug: print 'add_connect', c[0], c[1], c[2][0], c[2][1]
            add_connection (c[0], c[1], c[2][0], c[2][1])

# Increment the state machine by one step
def run_one_step(state_machine, state, step, action):
    if debug: print '\nstep:',step
    old_state = state
    state = transition (old_state, step)
    if state!=old_state: 
        action(old_state)
        if debug: print 'new state: ', state
    return state

# Do a sequence of events and return the final state
def run_sequence (state_machine, state, events, action):
    if debug: print 'events:', events
    for step in events:
        state = run_one_step(state_machine, state, step, action)
    return state
