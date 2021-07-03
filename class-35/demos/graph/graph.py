class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def get_nodes(self):
        return tuple(self.adjacency_list.keys())

    def size(self):
        return len(self.adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Vertex:
    def __init__(self, value):
        self.value = value
