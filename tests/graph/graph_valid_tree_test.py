import unittest

from problems.graph.graph_valid_tree import GraphValidTree


class TestGraphValidTree(unittest.TestCase):

    def test_valid_tree_single_node(self):
        graph_valid_tree = GraphValidTree()
        self.assertTrue(graph_valid_tree.validTree(1, []))

    def test_valid_tree_tree_structure(self):
        graph_valid_tree = GraphValidTree()
        self.assertTrue(graph_valid_tree.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))

    def test_valid_tree_cycle_exists(self):
        graph_valid_tree = GraphValidTree()
        self.assertFalse(graph_valid_tree.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

    def test_valid_tree_disconnected_graph(self):
        graph_valid_tree = GraphValidTree()
        self.assertFalse(graph_valid_tree.validTree(4, [[0, 1], [2, 3]]))

    def test_valid_tree_no_edges_multiple_nodes(self):
        graph_valid_tree = GraphValidTree()
        self.assertFalse(graph_valid_tree.validTree(4, []))


if __name__ == '__main__':
    unittest.main()
