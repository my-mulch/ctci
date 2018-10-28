from problems import chapter4

from tools.structures import graph
from tools.structures import binary_search_tree
from tools.structures import binary_tree

the_graph = graph.examples[0]
the_bst = binary_search_tree.examples[0]
the_bin_tree = binary_tree.examples[0]

start = the_bin_tree.root.right.right
target = the_bin_tree.root.right.left

print(chapter4.first_common_ancestor(the_bin_tree.root, target, start))
