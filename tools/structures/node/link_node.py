from .base_node import BaseNode

class DoubleLinkNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)
        
        self.next = None
        self.prev = None

class SingleLinkNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)
        
        self.next = None
        