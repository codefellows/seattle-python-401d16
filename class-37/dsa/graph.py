class Graph:
    def __init__(self):

        self._adjacency_list = {}

    def add_node(self, value):

        v = Vertex(value)

        self._adjacency_list[v] = []

        return v

    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):

        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not found in graph")

        adjacencies = self._adjacency_list[start_vertex]

        adjacencies.append(Edge(end_vertex, weight))

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, [])


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


if __name__ == "__main__":
    g = Graph()
    spam = g.add_node("spam")
    eggs = g.add_node("eggs")
    g.add_edge(spam, eggs)
