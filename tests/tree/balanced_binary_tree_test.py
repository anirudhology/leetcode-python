import unittest

from problems.tree.balanced_binary_tree import BalancedBinaryTree
from problems.util.tree_node import TreeNode


class BalancedBinaryTreeTest(unittest.TestCase):
    def test_isBalanced(self):
        balanced_binary_tree = BalancedBinaryTree()

        # Test case 1: Empty tree
        self.assertTrue(balanced_binary_tree.isBalanced(None))

        # Test case 2: Single node tree
        root1 = TreeNode(1)
        self.assertTrue(balanced_binary_tree.isBalanced(root1))

        # Test case 3: Balanced tree
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        self.assertTrue(balanced_binary_tree.isBalanced(root2))

        # Test case 4: Unbalanced tree
        root3 = TreeNode(1)
        root3.left = TreeNode(2)
        root3.left.left = TreeNode(3)
        self.assertFalse(balanced_binary_tree.isBalanced(root3))

        # Test case 5: Larger balanced tree
        root4 = TreeNode(1)
        root4.left = TreeNode(2)
        root4.right = TreeNode(3)
        root4.left.left = TreeNode(4)
        root4.left.right = TreeNode(5)
        root4.right.left = TreeNode(6)
        root4.right.right = TreeNode(7)
        self.assertTrue(balanced_binary_tree.isBalanced(root4))


if __name__ == '__main__':
    unittest.main()
