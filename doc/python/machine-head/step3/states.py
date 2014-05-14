#!/usr/bin/python
# Build a minimalistic state machine in python

#----------------------------------------------------------------------------------------
# State machine domain

# Advance the state machine based on the event
def transition(state_machine,state, event):
    key=state+'/'+event
    if (state_machine.has_key(key)):
        state = state_machine[key]
        return state
    return state

# Create edges in graph
def add_transition(state_machine,old_state, new_state, event):
    state_machine[old_state+'/'+event] = new_state

# Create all of the connectors to match the map
def create_machine(connect_map):
    state_machine = {}
    for connector in connect_map.split('\n')[1:-1]:
        c = connector.split(',')
        if len(c)==3:
            add_transition (state_machine, c[0], c[1], c[2])
    return state_machine

# Increment the state machine by one step
def run_one_step(state_machine, state, step, action):
    old_state = state
    state = transition (state_machine, old_state, step)
    if state!=old_state: 
        action(old_state)
    return state

# Do a sequence of events and return the final state
def run_sequence (state_machine, state, events, action):
    for step in events:
        state = run_one_step(state_machine, state, step, action)
    return state
