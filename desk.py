from problems import chapter4
from tools.structures import graph
from tools.structures import bst


A = graph.GraphNode(data=0, adjacent=[1, 4])
B = graph.GraphNode(data=1, adjacent=[2, 7])
C = graph.GraphNode(data=2, adjacent=[0])
D = graph.GraphNode(data=3, adjacent=[0, 1, 8])
E = graph.GraphNode(data=4, adjacent=[9])
F = graph.GraphNode(data=5, adjacent=[4, 6])
G = graph.GraphNode(data=6, adjacent=[])
H = graph.GraphNode(data=7, adjacent=[6, 8, 9])
I = graph.GraphNode(data=8, adjacent=[1, 7])
J = graph.GraphNode(data=9, adjacent=[1, 5, 6])

the_graph = graph.Graph(nodes=[A, B, C, D, E, F, G, H, I, J])


the_bst = bst.BST()

the_bst.insert(bst.BSTNode(11))
the_bst.insert(bst.BSTNode(14))
the_bst.insert(bst.BSTNode(13))
the_bst.insert(bst.BSTNode(6))
the_bst.insert(bst.BSTNode(3))
the_bst.insert(bst.BSTNode(5))
the_bst.insert(bst.BSTNode(8))
the_bst.insert(bst.BSTNode(15))

print(chapter4.check_balance(the_bst.root))
