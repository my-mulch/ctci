from .base_node import BaseNode

class BstNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)
        
        self.left = None
        self.right = None
