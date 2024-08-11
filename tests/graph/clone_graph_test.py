import unittest

from problems.graph.clone_graph import CloneGraph
from problems.util.graph_node import GraphNode


class TestCloneGraph(unittest.TestCase):

    def setUp(self):
        self.clone_graph = CloneGraph()

    def test_null_node(self):
        self.assertIsNone(self.clone_graph.cloneGraph(None))

    def test_single_node(self):
        node = GraphNode(1)
        clone = self.clone_graph.cloneGraph(node)
        self.assertIsNot(node, clone)
        self.assertEqual(node.val, clone.val)
        self.assertEqual(len(clone.neighbors), 0)

    def test_graph_with_one_edge(self):
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
        clone = self.clone_graph.cloneGraph(node1)

        self.assertIsNot(node1, clone)
        self.assertEqual(node1.val, clone.val)
        self.assertEqual(len(clone.neighbors), 1)
        self.assertEqual(clone.neighbors[0].val, 2)
        self.assertIsNot(node1.neighbors[0], clone.neighbors[0])

    def test_graph_with_cycle(self):
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node3 = GraphNode(3)
        node1.neighbors.append(node2)
        node2.neighbors.append(node3)
        node3.neighbors.append(node1)

        clone = self.clone_graph.cloneGraph(node1)

        self.assertIsNot(node1, clone)
        self.assertEqual(node1.val, clone.val)
        self.assertEqual(len(clone.neighbors), 1)
        self.assertEqual(clone.neighbors[0].val, 2)

        clone2 = clone.neighbors[0]
        self.assertEqual(clone2.neighbors[0].val, 3)
        self.assertEqual(clone2.neighbors[0].neighbors[0].val, 1)


if __name__ == '__main__':
    unittest.main()
