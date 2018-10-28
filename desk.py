from problems import chapter4, chapter1

from tools.structures import graph
from tools.structures import binary_search_tree
from tools.structures import binary_tree

the_graph = graph.examples[0]
the_bst = binary_search_tree.examples[0]
the_bin_tree = binary_tree.examples[0]

levels = [chapter1.get_perms(level, all_perms=[])
          for level in chapter4.level_lists(the_bin_tree)]


chapter4.bst_sequences(levels)
