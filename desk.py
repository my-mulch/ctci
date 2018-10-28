from problems import chapter4
from tools.structures.binary_tree import BinaryTree, BinaryTreeNode

import numpy as np

tree1 = np.random.randint(0, 10, 25).tolist()
tree2 = tree1.copy()

bin_tree_1 = BinaryTree(tree=tree1)
bin_tree_2 = BinaryTree(tree=tree2)


