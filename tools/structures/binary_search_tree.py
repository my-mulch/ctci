from .binary_tree import BinaryTreeNode, BinaryTree


class BinarySearchTree(BinaryTree):

    def __init__(self, tree=[]):
        super().__init__(tree)

    def insert(self, node):
        if type(node) is not BinaryTreeNode:
            node = BinaryTreeNode(node)

        if not self.root:
            self.root = node
            return

        cur = self.root

        while cur:
            child = 'left' if node.data <= cur.data else 'right'
            setattr(node, 'parent', cur)
            cur = getattr(cur, child)

        setattr(node.parent, child, node)


examples = [BinarySearchTree([11, 14, 13, 6, 3, 5, 8, 15])]
