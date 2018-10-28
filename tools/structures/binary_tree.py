from .base_node import BaseNode


class BinaryTreeNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)

        self.left = None
        self.right = None
        self.parent = None


class BinaryTree():

    def __init__(self, tree=[]):
        self.root = tree[0] = BinaryTreeNode(tree[0])
        if not len(tree) % 2:
            tree.append(None)

        for i in range(len(tree) // 2):
            node = tree[i]

            if tree[2 * i + 1] is not None:
                tree[2 * i + 1] = BinaryTreeNode(tree[2 * i + 1])
                node.left = tree[2 * i + 1]
                node.left.parent = node

            if tree[2 * i + 2] is not None:
                tree[2 * i + 2] = BinaryTreeNode(tree[2 * i + 2])
                node.right = tree[2 * i + 2]
                node.right.parent = node


examples = [BinaryTree([50, 25, 80, 15, 40, 60, 90, None,
                        None, 32, 44, None, None, None, None])]
