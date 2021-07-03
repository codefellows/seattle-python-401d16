"""

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

add node
Arguments: value
Returns: The added node
Add a node to the graph

add edge
Arguments: 2 nodes to be connected by the edge, weight (optional)
Returns: nothing
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph

get nodes
Arguments: none
Returns all of the nodes in the graph as a collection (set, list, or similar)

get neighbors
Arguments: node
Returns a collection of edges connected to the given node
Include the weight of the connection in the returned collection

size
Arguments: none
Returns the total number of nodes in the graph

TESTS

An empty graph properly returns null

"""
from graph import Graph, Vertex


def test_add_node():
    graph = Graph()

    expected_value = "spam"

    actual = graph.add_node("spam")

    assert actual.value == expected_value


def test_get_nodes_one():
    graph = Graph()

    graph.add_node("spam")

    actual = graph.get_nodes()

    expected = 1

    assert len(actual) == expected

    assert isinstance(actual[0], Vertex)

    assert actual[0].value == "spam"


# REFACTOR to not do so much
def test_get_nodes_two():
    graph = Graph()

    graph.add_node("spam")
    graph.add_node("eggs")

    actual = graph.get_nodes()

    expected = 2

    assert len(actual) == expected

    assert isinstance(actual[0], Vertex)
    assert isinstance(actual[1], Vertex)

    assert actual[0].value == "spam"
    assert actual[1].value == "eggs"


def test_size_two():
    graph = Graph()

    graph.add_node("spam")
    graph.add_node("eggs")

    actual = graph.size()
    expected = 2

    assert actual == expected


def test_add_edge_no_weight():
    graph = Graph()
    spam_vertex = graph.add_node("spam")
    eggs_vertex = graph.add_node("eggs")

    return_val = graph.add_edge(spam_vertex, eggs_vertex)

    assert return_val is None


def test_get_neighbors():
    graph = Graph()
    spam_vertex = graph.add_node("spam")
    eggs_vertex = graph.add_node("eggs")

    graph.add_edge(spam_vertex, eggs_vertex, 5)

    neighbors = graph.get_neighbors(spam_vertex)

    assert len(neighbors) == 1

    single_edge = neighbors[0]

    assert single_edge.vertex.value == "eggs"
    assert single_edge.weight == 5


def test_get_neighbors_solo():
    graph = Graph()
    spam_vertex = graph.add_node("spam")

    graph.add_edge(spam_vertex, spam_vertex)

    neighbors = graph.get_neighbors(spam_vertex)

    assert len(neighbors) == 1

    single_edge = neighbors[0]

    assert single_edge.vertex.value == "spam"
    assert single_edge.weight == 0
