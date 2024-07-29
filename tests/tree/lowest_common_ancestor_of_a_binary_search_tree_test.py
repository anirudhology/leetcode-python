import unittest

from problems.tree.lowest_common_ancestor_of_a_binary_search_tree import LowestCommonAncestorOfABinarySearchTree
from problems.util.tree_node import TreeNode


class LowestCommonAncestorOfABinarySearchTreeTest(unittest.TestCase):
    # noinspection PyTypeChecker
    def test_lowest_common_ancestor(self):
        lowest_common_ancestor_of_a_binary_search_tree = LowestCommonAncestorOfABinarySearchTree()

        # Test case 1: Both nodes are null
        self.assertIsNone(lowest_common_ancestor_of_a_binary_search_tree.lowestCommonAncestor(None, None, None))

        # Test case 2: One node is null
        root = TreeNode(3)
        p = TreeNode(1)
        self.assertIsNone(lowest_common_ancestor_of_a_binary_search_tree.lowestCommonAncestor(root, None, p))
        self.assertIsNone(lowest_common_ancestor_of_a_binary_search_tree.lowestCommonAncestor(root, p, None))

        # Test case 3: Both nodes are the same
        self.assertEqual(lowest_common_ancestor_of_a_binary_search_tree.lowestCommonAncestor(p, p, p), p)

        # Test case 4: LCA is root
        q = TreeNode(5)
        root.left = p
        root.right = q
        self.assertEqual(lowest_common_ancestor_of_a_binary_search_tree.lowestCommonAncestor(root, p, q), root)

        # Test case 5: LCA is in the left subtree
        p2 = TreeNode(0)
        p.left = p2
        self.assertEqual(lowest_common_ancestor_of_a_binary_search_tree.lowestCommonAncestor(root, p2, p), p)

        # Test case 6: LCA is in the right subtree
        q2 = TreeNode(6)
        q.right = q2
        self.assertEqual(lowest_common_ancestor_of_a_binary_search_tree.lowestCommonAncestor(root, q, q2), q)

        # Test case 7: Complex tree
        root2 = TreeNode(6)
        p3 = TreeNode(2)
        q3 = TreeNode(8)
        root2.left = TreeNode(0)
        root2.right = TreeNode(4)
        root2.left.left = TreeNode(3)
        root2.left.right = TreeNode(5)
        self.assertEqual(lowest_common_ancestor_of_a_binary_search_tree.lowestCommonAncestor(root2, p3, q3), root2)


if __name__ == '__main__':
    unittest.main()
