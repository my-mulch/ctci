from problems import chapter4

from tools.structures import graph
from tools.structures import binary_search_tree
from tools.structures import binary_tree

the_graph = graph.examples[0]
the_bst = binary_search_tree.examples[0]
the_bin_tree = binary_tree.examples[0]

print(chapter4.successor(the_bin_tree.root.left.left.right))

