import unittest

from problems.tree.invert_binary_tree import InvertBinaryTree
from problems.util.tree_node import TreeNode


class InvertBinaryTreeTest(unittest.TestCase):
    def test_invertTree(self):
        ibt = InvertBinaryTree()

        # Test case 1: Empty tree
        self.assertIsNone(ibt.invertTree(None))

        # Test case 2: Single node tree
        root1 = TreeNode(1)
        result1 = ibt.invertTree(root1)
        self.assertEqual(result1.val, 1)
        self.assertIsNone(result1.left)
        self.assertIsNone(result1.right)

        # Test case 3: Full binary tree
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        root2.left.left = TreeNode(4)
        root2.left.right = TreeNode(5)
        root2.right.left = TreeNode(6)
        root2.right.right = TreeNode(7)

        inverted_root2 = ibt.invertTree(root2)
        self.assertEqual(inverted_root2.val, 1)
        self.assertEqual(inverted_root2.left.val, 3)
        self.assertEqual(inverted_root2.right.val, 2)
        self.assertEqual(inverted_root2.left.left.val, 7)
        self.assertEqual(inverted_root2.left.right.val, 6)
        self.assertEqual(inverted_root2.right.left.val, 5)
        self.assertEqual(inverted_root2.right.right.val, 4)


if __name__ == '__main__':
    unittest.main()
