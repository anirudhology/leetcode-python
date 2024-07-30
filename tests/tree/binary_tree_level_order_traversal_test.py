import unittest

from problems.tree.binary_tree_level_order_traversal import BinaryTreeLevelOrderTraversal
from problems.util.tree_node import TreeNode


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):

    def test_level_order(self):
        binary_tree_level_order_traversal = BinaryTreeLevelOrderTraversal()

        # Test case 1: Empty tree
        root1 = None
        result1 = binary_tree_level_order_traversal.levelOrder(root1)
        self.assertEqual(result1, [])

        # Test case 2: Single node tree
        root2 = TreeNode(1)
        expected2 = [[1]]
        result2 = binary_tree_level_order_traversal.levelOrder(root2)
        self.assertEqual(result2, expected2)

        # Test case 3: Tree with two levels
        root3 = TreeNode(1)
        root3.left = TreeNode(2)
        root3.right = TreeNode(3)
        expected3 = [[1], [2, 3]]
        result3 = binary_tree_level_order_traversal.levelOrder(root3)
        self.assertEqual(result3, expected3)

        # Test case 4: Tree with three levels
        root4 = TreeNode(1)
        root4.left = TreeNode(2)
        root4.right = TreeNode(3)
        root4.left.left = TreeNode(4)
        root4.left.right = TreeNode(5)
        root4.right.left = TreeNode(6)
        root4.right.right = TreeNode(7)
        expected4 = [[1], [2, 3], [4, 5, 6, 7]]
        result4 = binary_tree_level_order_traversal.levelOrder(root4)
        self.assertEqual(result4, expected4)


if __name__ == '__main__':
    unittest.main()
