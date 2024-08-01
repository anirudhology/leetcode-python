import unittest

from problems.tree.serialize_and_deserialize_binary_tree import SerializeAndDeserializeBinaryTree
from problems.util.tree_node import TreeNode


class TestSerializeAndDeserializeBinaryTree(unittest.TestCase):

    def test_serialize_and_deserialize(self):
        codec = SerializeAndDeserializeBinaryTree.Codec()

        # Test case 1: Empty tree
        root1 = None
        # noinspection PyTypeChecker
        self.assertEqual(codec.serialize(root1), "")
        self.assertIsNone(codec.deserialize(""))

        # Test case 2: Single node tree
        root2 = TreeNode(1)
        self.assertEqual(codec.serialize(root2), "1 n n")
        result2 = codec.deserialize("1 n n")
        self.assertEqual(result2.val, '1')
        self.assertIsNone(result2.left)
        self.assertIsNone(result2.right)

        # Test case 3: Complete binary tree
        root3 = TreeNode(1)
        root3.left = TreeNode(2)
        root3.right = TreeNode(3)
        root3.left.left = TreeNode(4)
        root3.left.right = TreeNode(5)
        root3.right.left = TreeNode(6)
        root3.right.right = TreeNode(7)
        serialized3 = codec.serialize(root3)
        self.assertEqual(serialized3, "1 2 3 4 5 6 7 n n n n n n n n")
        result3 = codec.deserialize(serialized3)
        self.assertEqual(result3.val, '1')
        self.assertEqual(result3.left.val, 2)
        self.assertEqual(result3.right.val, 3)
        self.assertEqual(result3.left.left.val, 4)
        self.assertEqual(result3.left.right.val, 5)
        self.assertEqual(result3.right.left.val, 6)
        self.assertEqual(result3.right.right.val, 7)

        # Test case 4: Tree with only left children
        root4 = TreeNode(1)
        root4.left = TreeNode(2)
        root4.left.left = TreeNode(3)
        root4.left.left.left = TreeNode(4)
        serialized4 = codec.serialize(root4)
        self.assertEqual(serialized4, "1 2 n 3 n 4 n n n")
        result4 = codec.deserialize(serialized4)
        self.assertEqual(result4.val, '1')
        self.assertEqual(result4.left.val, 2)
        self.assertIsNone(result4.right)
        self.assertEqual(result4.left.left.val, 3)
        self.assertIsNone(result4.left.right)
        self.assertEqual(result4.left.left.left.val, 4)
        self.assertIsNone(result4.left.left.right)

        # Test case 5: Tree with only right children
        root5 = TreeNode(1)
        root5.right = TreeNode(2)
        root5.right.right = TreeNode(3)
        root5.right.right.right = TreeNode(4)
        serialized5 = codec.serialize(root5)
        self.assertEqual(serialized5, "1 n 2 n 3 n 4 n n")
        result5 = codec.deserialize(serialized5)
        self.assertEqual(result5.val, '1')
        self.assertIsNone(result5.left)
        self.assertEqual(result5.right.val, 2)
        self.assertIsNone(result5.right.left)
        self.assertEqual(result5.right.right.val, 3)
        self.assertIsNone(result5.right.right.left)
        self.assertEqual(result5.right.right.right.val, 4)
        self.assertIsNone(result5.right.right.right.right)


if __name__ == "__main__":
    unittest.main()
