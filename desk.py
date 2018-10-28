from problems import chapter4
from tools.structures.binary_tree import BinaryTree, BinaryTreeNode

import numpy as np

tree = BinaryTree(tree=[7, -2, 3, -1, 4, 6, 1, 5, 6, None, None, 1, 4])

chapter4.path_sums(tree.root, 10)
