import unittest

from problems.tree.binary_tree_right_side_view import BinaryTreeRightSideView
from problems.util.tree_node import TreeNode


class BinaryTreeRightSideViewTest(unittest.TestCase):

    def setUp(self):
        self.binary_tree_right_side_view = BinaryTreeRightSideView()

    def test_empty_tree(self):
        self.assertEqual(self.binary_tree_right_side_view.rightSideView(None), [])

    def test_single_node_tree(self):
        root = TreeNode(1)
        self.assertEqual(self.binary_tree_right_side_view.rightSideView(root), [1])

    def test_right_leaning_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.binary_tree_right_side_view.rightSideView(root), [1, 2, 3])

    def test_left_leaning_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(self.binary_tree_right_side_view.rightSideView(root), [1, 2, 3])

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertEqual(self.binary_tree_right_side_view.rightSideView(root), [1, 3, 6])


if __name__ == '__main__':
    unittest.main()
