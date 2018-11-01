from .base_node import BaseNode


class GraphNode(BaseNode):
    def __init__(self, data, adjacent=None):
        super().__init__(data)

        self.visited = False
        self.adjacent = adjacent if adjacent else list()
        self.incoming_edges = 0


class Graph():

    def __init__(self, nodes=[]):
        self.nodes = nodes

    def insert(self, node):
        if type(node) is not GraphNode:
            node = GraphNode(node)

        self.nodes.append(node)

    @staticmethod
    def depth_first_iterative(S):
        stack = [S]
        visited = set()

        while stack:
            cur = stack[-1]

            if cur.adjacent:
                child = cur.adjacent.pop()
                if child not in visited:
                    print(child)
                    stack.append(child)
                    visited.add(child)
            else:
                stack.pop()  # finish node

    @staticmethod
    def breadth_first_search(S, E):
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
        GraphNode(data='S', adjacent=[1, 2, 3]),
        GraphNode(data='A', adjacent=[2, 7]),
        GraphNode(data='B', adjacent=[3, 4]),
        GraphNode(data='C', adjacent=[5]),
        GraphNode(data='D', adjacent=[3, 5]),
        GraphNode(data='E', adjacent=[]),
    ])
]
