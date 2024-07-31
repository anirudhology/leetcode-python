import unittest

from problems.tree.construct_binary_tree_from_preorder_and_inorder_traversal import \
    ConstructBinaryTreeFromPreorderAndInorderTraversal


class ConstructBinaryTreeFromPreorderAndInorderTraversalTest(unittest.TestCase):

    def setUp(self):
        self.construct_binary_tree_from_preorder_and_inorder_traversal = (
            ConstructBinaryTreeFromPreorderAndInorderTraversal())

    def test_build_tree_single_node(self):
        preorder = [1]
        inorder = [1]
        root = self.construct_binary_tree_from_preorder_and_inorder_traversal.buildTree(preorder, inorder)
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_build_tree_two_nodes(self):
        preorder = [1, 2]
        inorder = [2, 1]
        root = self.construct_binary_tree_from_preorder_and_inorder_traversal.buildTree(preorder, inorder)
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 1)
        self.assertIsNotNone(root.left)
        self.assertEqual(root.left.val, 2)
        self.assertIsNone(root.right)

    def test_build_tree_balanced_tree(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        root = self.construct_binary_tree_from_preorder_and_inorder_traversal.buildTree(preorder, inorder)
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 3)
        self.assertIsNotNone(root.left)
        self.assertEqual(root.left.val, 9)
        self.assertIsNotNone(root.right)
        self.assertEqual(root.right.val, 20)

    def test_build_tree_empty_tree(self):
        preorder = []
        inorder = []
        root = self.construct_binary_tree_from_preorder_and_inorder_traversal.buildTree(preorder, inorder)
        self.assertIsNone(root)

    def test_build_tree_unbalanced_tree(self):
        preorder = [3, 2, 1, 4, 5]
        inorder = [1, 2, 3, 4, 5]
        root = self.construct_binary_tree_from_preorder_and_inorder_traversal.buildTree(preorder, inorder)
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 3)
        self.assertIsNotNone(root.left)
        self.assertEqual(root.left.val, 2)
        self.assertIsNotNone(root.left.left)
        self.assertEqual(root.left.left.val, 1)
        self.assertIsNotNone(root.right)
        self.assertEqual(root.right.val, 4)
        self.assertIsNotNone(root.right.right)
        self.assertEqual(root.right.right.val, 5)


if __name__ == '__main__':
    unittest.main()
