from tools.structures import graph

S = graph.GraphNode('S')
A = graph.GraphNode('A')
B = graph.GraphNode('B')
C = graph.GraphNode('C')
D = graph.GraphNode('D')
E = graph.GraphNode('E')

S.adjacent = [A, B, C]
B.adjacent = [C, D]
C.adjacent = [E]
D.adjacent = [C, E]


graph.Graph.depth_first_iterative(S)
