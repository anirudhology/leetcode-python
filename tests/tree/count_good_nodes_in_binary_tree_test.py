import unittest

from problems.tree.count_good_nodes_in_binary_tree import CountGoodNodesInBinaryTree
from problems.util.tree_node import TreeNode


class TestGoodNodesInBinaryTree(unittest.TestCase):

    def setUp(self):
        self.count_good_nodes_in_binary_tree = CountGoodNodesInBinaryTree()

    def test_single_node_tree(self):
        root = TreeNode(1)
        self.assertEqual(self.count_good_nodes_in_binary_tree.goodNodes(root), 1)

    def test_right_leaning_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.count_good_nodes_in_binary_tree.goodNodes(root), 3)

    def test_left_leaning_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        self.assertEqual(self.count_good_nodes_in_binary_tree.goodNodes(root), 1)

    def test_balanced_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.left = TreeNode(3)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        self.assertEqual(self.count_good_nodes_in_binary_tree.goodNodes(root), 4)


if __name__ == '__main__':
    unittest.main()
