from node.bst_node import BstNode

class BST():

    def __init__(self, root=None):
        self.root = root
    
    def insert(self, node):
        cur = self.root
        parent = cur

        while cur:
            if node.data <= cur.data:
                parent = (cur, 'lChild')
                cur = cur.lChild
            else:
                parent = (cur, 'rChild')
                cur = cur.rChild
        
        parent, child = parent
        parent[child] = node

        

        

        