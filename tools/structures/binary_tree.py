from .base_node import BaseNode


class BinaryTreeNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)

        self.left = None
        self.right = None
        self.parent = None


class BinaryTree():

    def __init__(self, tree=[]):
        self.root = None
        
        if tree:
            self.root = BinaryTreeNode(tree[0])
            
            if not len(tree) % 2: # saves index out of bounds
                tree.append(None)

        for i in range(len(tree) // 2):
            node = tree[i] if i > 0 else self.root
            node.left = tree[2 * i + 1] = BinaryTreeNode(tree[2 * i + 1])
            node.right = tree[2 * i + 2] = BinaryTreeNode(tree[2 * i + 2])

examples = [BinaryTree([11, 9, 14, 6, 10, 12, 16, 2])]
