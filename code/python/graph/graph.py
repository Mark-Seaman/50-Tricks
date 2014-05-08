#!/usr/bin/env python
# Build a graph data structure

graph = {}

# Add one edge to the graph
def add(source,dest):
    if graph.has_key(source):
        if dest not in graph[source]:
            graph[source].append(dest)
    else:
        graph[source] = [dest]

# Lookup a node in the graph
def lookup(node):
    if graph.has_key(node): return graph[node]

# Print the entire graph
def print_graph(graph):
    for n in graph:
        print ','.join([n]+graph[n])

# Build a graph from CSV text
def build_graph(text):
    for line in text.split('\n'): 
        list = line.split(',')
        for i in list[1:]:
            #print 'ADD:', list[0], i
            add(list[0], i)
    return graph
