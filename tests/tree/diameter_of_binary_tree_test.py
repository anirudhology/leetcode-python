import unittest

from problems.tree.diameter_of_binary_tree import DiameterOfBinaryTree
from problems.util.tree_node import TreeNode


class DiameterOfBinaryTreeTest(unittest.TestCase):
    def test_diameterOfBinaryTree(self):
        dbt = DiameterOfBinaryTree()

        # Test case 1: Empty tree
        self.assertEqual(dbt.diameterOfBinaryTree(None), 0)

        # Test case 2: Single node tree
        root1 = TreeNode(1)
        self.assertEqual(dbt.diameterOfBinaryTree(root1), 0)

        # Test case 3: Two-level tree
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        self.assertEqual(dbt.diameterOfBinaryTree(root2), 1)

        # Test case 4: Full binary tree
        root3 = TreeNode(1)
        root3.left = TreeNode(2)
        root3.right = TreeNode(3)
        root3.left.left = TreeNode(4)
        root3.left.right = TreeNode(5)
        self.assertEqual(dbt.diameterOfBinaryTree(root3), 3)

        # Test case 5: Larger tree
        root4 = TreeNode(1)
        root4.left = TreeNode(2)
        root4.right = TreeNode(3)
        root4.left.left = TreeNode(4)
        root4.left.right = TreeNode(5)
        root4.right.right = TreeNode(6)
        root4.left.left.left = TreeNode(7)
        self.assertEqual(dbt.diameterOfBinaryTree(root4), 5)


if __name__ == '__main__':
    unittest.main()
