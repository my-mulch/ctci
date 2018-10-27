from .base_node import BaseNode


class GraphNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)

        self.visited = True
        self.adjacent = []


class Graph():

    def __init__(self, nodes=[]):
        self.nodes = nodes

    def insert(self, node):
        if type(node) is not GraphNode:
            node = GraphNode(node)

        self.nodes.append(node)
