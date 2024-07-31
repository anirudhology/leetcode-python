import unittest

from problems.tree.validate_binary_search_tree import ValidateBinarySearchTree
from problems.util.tree_node import TreeNode


class TestValidateBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.validate_binary_search_tree = ValidateBinarySearchTree()

    def test_empty_tree(self):
        self.assertTrue(self.validate_binary_search_tree.isValidBST(None))

    def test_single_node_tree(self):
        root = TreeNode(1)
        self.assertTrue(self.validate_binary_search_tree.isValidBST(root))

    def test_valid_bst(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(self.validate_binary_search_tree.isValidBST(root))

    def test_invalid_bst(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(self.validate_binary_search_tree.isValidBST(root))

    def test_valid_bst_with_negative_values(self):
        root = TreeNode(0)
        root.left = TreeNode(-1)
        self.assertTrue(self.validate_binary_search_tree.isValidBST(root))

    def test_invalid_bst_with_equal_values(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        self.assertFalse(self.validate_binary_search_tree.isValidBST(root))


if __name__ == '__main__':
    unittest.main()
