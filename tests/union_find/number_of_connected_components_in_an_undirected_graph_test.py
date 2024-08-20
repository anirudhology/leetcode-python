import unittest

from problems.union_find.number_of_connected_components_in_an_undirected_graph import \
    NumberOfConnectedComponentsInAnUndirectedGraph


class TestNumberOfConnectedComponents(unittest.TestCase):

    def test_no_edges(self):
        graph = NumberOfConnectedComponentsInAnUndirectedGraph()
        edges = []
        self.assertEqual(graph.countComponents(4, edges), 4)

    def test_fully_connected_graph(self):
        graph = NumberOfConnectedComponentsInAnUndirectedGraph()
        edges = [[0, 1], [1, 2], [2, 3]]
        self.assertEqual(graph.countComponents(4, edges), 1)

    def test_multiple_components(self):
        graph = NumberOfConnectedComponentsInAnUndirectedGraph()
        edges = [[0, 1], [2, 3]]
        self.assertEqual(graph.countComponents(4, edges), 2)

    def test_single_node(self):
        graph = NumberOfConnectedComponentsInAnUndirectedGraph()
        edges = []
        self.assertEqual(graph.countComponents(1, edges), 1)

    def test_empty_graph(self):
        graph = NumberOfConnectedComponentsInAnUndirectedGraph()
        edges = []
        self.assertEqual(graph.countComponents(0, edges), 0)


if __name__ == "__main__":
    unittest.main()
