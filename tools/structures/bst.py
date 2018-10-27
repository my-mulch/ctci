from .base_node import BaseNode

class BSTNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)

        self.left = None
        self.right = None
        self.parent = None


class BST():

    def __init__(self, root=None):
        self.root = root
    
    def insert(self, node):
        if type(node) is not BSTNode:
            node = BSTNode(node)

        if not self.root:
            self.root = node
            return
            
        cur = self.root
        
        while cur:
            child = 'left' if node.data <= cur.data else 'right'
            setattr(node, 'parent', cur)
            cur = getattr(cur, child)
        
        setattr(node.parent, child, node)
