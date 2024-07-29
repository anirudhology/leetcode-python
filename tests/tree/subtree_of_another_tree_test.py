import unittest

from problems.tree.subtree_of_another_tree import SubtreeOfAnotherTree
from problems.util.tree_node import TreeNode


class SubtreeOfAnotherTreeTest(unittest.TestCase):
    def test_isSubtree(self):
        subtree_of_another_tree = SubtreeOfAnotherTree()

        # Test case 1: Both trees are null
        self.assertFalse(subtree_of_another_tree.isSubtree(None, None))

        # Test case 2: One tree is null
        root1 = TreeNode(1)
        self.assertFalse(subtree_of_another_tree.isSubtree(root1, None))
        self.assertFalse(subtree_of_another_tree.isSubtree(None, root1))

        # Test case 3: Both trees have one node with the same value
        root2 = TreeNode(1)
        sub_root2 = TreeNode(1)
        self.assertTrue(subtree_of_another_tree.isSubtree(root2, sub_root2))

        # Test case 4: Subtree with different values
        root3 = TreeNode(1)
        sub_root3 = TreeNode(2)
        self.assertFalse(subtree_of_another_tree.isSubtree(root3, sub_root3))

        # Test case 5: Subtree is an actual subtree
        root4 = TreeNode(3)
        root4.left = TreeNode(4)
        root4.right = TreeNode(5)
        root4.left.left = TreeNode(1)
        root4.left.right = TreeNode(2)

        sub_root4 = TreeNode(4)
        sub_root4.left = TreeNode(1)
        sub_root4.right = TreeNode(2)
        self.assertTrue(subtree_of_another_tree.isSubtree(root4, sub_root4))

        # Test case 6: Subtree is not an actual subtree
        sub_root5 = TreeNode(4)
        sub_root5.left = TreeNode(1)
        sub_root5.right = TreeNode(3)
        self.assertFalse(subtree_of_another_tree.isSubtree(root4, sub_root5))


if __name__ == '__main__':
    unittest.main()
