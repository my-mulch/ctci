from .node.bst_node import BstNode

class BST():

    def __init__(self, root=None):
        self.root = root
    
    def insert(self, node):
        if type(node) is not BstNode:
            node = BstNode(node)

        cur = self.root
        parent = cur

        while cur:
            path = 'left' if node.data <= cur.data else 'right'
            parent = cur, path
            cur = getattr(cur, path)
        
        parent, child = parent
        setattr(parent, child, node)
