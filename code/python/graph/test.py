from graph import build_graph, print_graph, lookup

def test():
    graph_text = '''source1,dest1,dest2
source2,dest1,abc,dest2,abc'''
    graph = build_graph(graph_text)
    print_graph(graph)
    
    print lookup ('source')
    print lookup ('source1')
    print lookup ('source2')

test()


