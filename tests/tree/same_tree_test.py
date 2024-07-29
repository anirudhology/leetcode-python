import unittest

from problems.tree.same_tree import SameTree
from problems.util.tree_node import TreeNode


class TestSameTree(unittest.TestCase):
    def test_isSameTree(self):
        same_tree = SameTree()

        # Test case 1: Both trees are null
        self.assertTrue(same_tree.isSameTree(None, None))

        # Test case 2: One tree is null
        p1 = TreeNode(1)
        self.assertFalse(same_tree.isSameTree(p1, None))
        self.assertFalse(same_tree.isSameTree(None, p1))

        # Test case 3: Both trees have one node with the same value
        p2 = TreeNode(1)
        q2 = TreeNode(1)
        self.assertTrue(same_tree.isSameTree(p2, q2))

        # Test case 4: Both trees have one node with different values
        p3 = TreeNode(1)
        q3 = TreeNode(2)
        self.assertFalse(same_tree.isSameTree(p3, q3))

        # Test case 5: Both trees have multiple nodes with the same structure and values
        p4 = TreeNode(1)
        p4.left = TreeNode(2)
        p4.right = TreeNode(3)
        q4 = TreeNode(1)
        q4.left = TreeNode(2)
        q4.right = TreeNode(3)
        self.assertTrue(same_tree.isSameTree(p4, q4))

        # Test case 6: Both trees have multiple nodes with different structures
        p5 = TreeNode(1)
        p5.left = TreeNode(2)
        q5 = TreeNode(1)
        q5.right = TreeNode(2)
        self.assertFalse(same_tree.isSameTree(p5, q5))


if __name__ == '__main__':
    unittest.main()
