from .node.node import BstNode

class BST():

    def __init__(self, root=None):
        self.root = root
    
    def insert(self, node):
        if type(node) is not BstNode:
            node = BstNode(node)

        if not self.root:
            self.root = node
            return
            
        cur = self.root
        
        while cur:
            child = 'left' if node.data <= cur.data else 'right'
            setattr(node, 'parent', cur)
            cur = getattr(cur, child)
        
        setattr(node.parent, child, node)
