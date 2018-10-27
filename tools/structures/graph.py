from .node.graph_node import GraphNode


class Graph():

    def __init__(self, nodes=[]):
        self.nodes = nodes

    def insert(self, node):
        if type(node) is not GraphNode:
            node = GraphNode(node)

        self.nodes.append(node)
