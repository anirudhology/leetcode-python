import unittest

from problems.tree.kth_smallest_element_in_a_bst import KthSmallestElementInABST
from problems.util.tree_node import TreeNode


class KthSmallestElementInABSTTest(unittest.TestCase):

    def setUp(self):
        self.kth_smallest_element_in_a_bst = KthSmallestElementInABST()

    def test_kth_smallest_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.kth_smallest_element_in_a_bst.kthSmallest(root, 1), 1)

    def test_kth_smallest_left_skewed_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        self.assertEqual(self.kth_smallest_element_in_a_bst.kthSmallest(root, 2), 2)

    def test_kth_smallest_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.kth_smallest_element_in_a_bst.kthSmallest(root, 3), 3)

    def test_kth_smallest_balanced_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(self.kth_smallest_element_in_a_bst.kthSmallest(root, 3), 3)

    def test_kth_smallest_k_greater_than_nodes(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.kth_smallest_element_in_a_bst.kthSmallest(root, 4),
                         0)  # This assumes we have a condition to handle this gracefully


if __name__ == '__main__':
    unittest.main()
