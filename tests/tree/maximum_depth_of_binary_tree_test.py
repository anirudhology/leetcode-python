import unittest

from problems.tree.maximum_depth_of_binary_tree import MaximumDepthOfBinaryTree
from problems.util.tree_node import TreeNode


class MaximumDepthOfBinaryTreeTest(unittest.TestCase):
    def test_maxDepth(self):
        maximum_depth_of_binary_tree = MaximumDepthOfBinaryTree()

        # Test case 1: Empty tree
        self.assertEqual(maximum_depth_of_binary_tree.maxDepth(None), 0)

        # Test case 2: Single node tree
        root1 = TreeNode(1)
        self.assertEqual(maximum_depth_of_binary_tree.maxDepth(root1), 1)

        # Test case 3: Two-level tree
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        self.assertEqual(maximum_depth_of_binary_tree.maxDepth(root2), 2)

        # Test case 4: Full binary tree
        root3 = TreeNode(1)
        root3.left = TreeNode(2)
        root3.right = TreeNode(3)
        root3.left.left = TreeNode(4)
        root3.left.right = TreeNode(5)
        root3.right.left = TreeNode(6)
        root3.right.right = TreeNode(7)
        self.assertEqual(maximum_depth_of_binary_tree.maxDepth(root3), 3)


if __name__ == '__main__':
    unittest.main()
