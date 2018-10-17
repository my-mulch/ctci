from node.bst_node import BstNode

class BST():

    def __init__(self, root=None):
        self.root = root
    
    def insert(self, node):
        if type(node) is not BstNode:
            node = BstNode(node)

        cur = self.root
        parent = cur

        while cur:
            if node.data <= cur.data:
                parent = (cur, 'left')
                cur = cur.left
            else:
                parent = (cur, 'right')
                cur = cur.right
        
        parent, child = parent
        setattr(parent, child, node)

    