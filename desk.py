from problems import chapter4

from tools.structures import graph
from tools.structures import binary_search_tree
from tools.structures import binary_tree

the_graph = graph.examples[0]
the_bst = binary_search_tree.examples[0]
the_bin_tree = binary_tree.examples[0]


A = graph.GraphNode('A')
B = graph.GraphNode('B')
C = graph.GraphNode('C')
D = graph.GraphNode('D')
E = graph.GraphNode('E')
F = graph.GraphNode('F')
G = graph.GraphNode('G')
H = graph.GraphNode('H')
I = graph.GraphNode('I')


chapter4.build_order(projects=[A, B, C, D, E, F, G, H, I],
                     dependencies=[(C, A), (C, B), (B, F), (G, E), (F, H), (H, I), (E, C), (E, D), (D, C)])
