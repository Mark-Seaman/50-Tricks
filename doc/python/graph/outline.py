#!/usr/bin/env python
# Create an outline for brain topics

from sys        import argv

from links      import get_file_links, has_file
from graph      import add, print_graph, lookup, build_graph, graph

link_table = []
printed = set()

# Build a tree of links
def build_link_tree(line):
    list = line.split(',')
    for i in list[1:]:
        add(list[0], i)
        brain_links(i)

# Read the links in this brain file
def brain_links(file):
    dir = "/home/seaman/Documents/Brain/"
    if not lookup(file) and has_file(dir+file):
        links = get_file_links(dir+file)
        build_graph(file+','+','.join(links))
        link_table.append([file]+links)
        for doc in links:
            if doc: brain_links(doc)

# Print indented strings
def print_indent(node,depth):
    indent = ''.join(['    ' for i in range(depth)])
    print '\n', indent, node,

# Print a nested outline of topics
def print_outline(node, depth, max_depth):
    if not lookup(node) or depth>max_depth: return
    if node in printed:
        print_indent(node+'*',depth)
    else:
        printed.add(node)    
        print_indent(node,depth)
        for n in lookup(node):
            print_outline(n, depth+1, max_depth)

# Build and print an outline of the links for a topic
if len(argv)<2:
    print 'Usage: outline Brain 3'
else:
    max_depth = 3
    topic = argv[1]
    if len(argv)>2: max_depth = int(argv[2])
    brain_links(topic)
    print_outline(topic,0,max_depth)

