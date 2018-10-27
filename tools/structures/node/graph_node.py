from .node import BaseNode


class GraphNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)

        self.visited = True
        self.adjacent = []
