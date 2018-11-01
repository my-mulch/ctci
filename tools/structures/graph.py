from .base_node import BaseNode


class GraphNode(BaseNode):
    def __init__(self, data, adjacent=None):
        super().__init__(data)

        self.visited = False
        self.adjacent = adjacent if adjacent else set()
        self.incoming_edges = 0


class Graph():

    def __init__(self, nodes=[]):
        self.nodes = nodes

    def insert(self, node):
        if type(node) is not GraphNode:
            node = GraphNode(node)

        self.nodes.append(node)

    @classmethod
    def breadth_first_search(graph, S, E):
        parent = {S: None}
        level = {S: 0}
        frontier = [S]
        i = 1

        while frontier:
            next_level = []
            for u in frontier:
                for v in u.adjacent:
                    if v not in level:
                        level[v] = i
                        parent[v] = u
                        next_level.append(v)

            frontier = next_level
            i += 1


examples = [
    Graph(nodes=[
        GraphNode(data='A', adjacent=[1, 4]),
        GraphNode(data='B', adjacent=[2, 7]),
        GraphNode(data='C', adjacent=[0]),
        GraphNode(data='D', adjacent=[0, 1, 8]),
        GraphNode(data='E', adjacent=[9]),
        GraphNode(data='F', adjacent=[4, 6]),
        GraphNode(data='G', adjacent=[]),
        GraphNode(data='H', adjacent=[6, 8, 9]),
        GraphNode(data='I', adjacent=[1, 7]),
        GraphNode(data='J', adjacent=[1, 5, 6])
    ])
]
