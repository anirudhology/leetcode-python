import unittest

from problems.tree.binary_tree_maximum_path_sum import BinaryTreeMaximumPathSum
from problems.util.tree_node import TreeNode


class BinaryTreeMaximumPathSumTest(unittest.TestCase):

    def setUp(self):
        self.binary_tree_maximum_path_sum = BinaryTreeMaximumPathSum()

    def test_max_path_sum_single_node(self):
        root = TreeNode(1)
        result = self.binary_tree_maximum_path_sum.maxPathSum(root)
        self.assertEqual(result, 1)

    def test_max_path_sum_two_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        result = self.binary_tree_maximum_path_sum.maxPathSum(root)
        self.assertEqual(result, 3)

    def test_max_path_sum_negative_nodes(self):
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        result = self.binary_tree_maximum_path_sum.maxPathSum(root)
        self.assertEqual(result, 42)

    def test_max_path_sum_mixed_values(self):
        root = TreeNode(2)
        root.left = TreeNode(-1)
        root.right = TreeNode(-2)
        result = self.binary_tree_maximum_path_sum.maxPathSum(root)
        self.assertEqual(result, 2)

    def test_max_path_sum_empty_tree(self):
        root = None
        result = self.binary_tree_maximum_path_sum.maxPathSum(root)
        self.assertEqual(result, float('-inf'))  # Equivalent to Integer.MIN_VALUE in Python


if __name__ == '__main__':
    unittest.main()
