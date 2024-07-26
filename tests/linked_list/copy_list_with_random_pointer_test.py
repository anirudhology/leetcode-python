import unittest

from problems.linked_list.copy_list_with_random_pointer import CopyListWithRandomPointer
from problems.util.list_node_with_random import ListNodeWithRandom


class CopyListWithRandomPointerTest(unittest.TestCase):

    @staticmethod
    def list_to_array(head):
        """Helper method to convert a list to an array representation for easier assertions."""
        array = []
        random_indices = []
        temp = head
        index_map = {}
        index = 0
        while temp:
            array.append(temp.val)
            index_map[temp] = index
            temp = temp.next
            index += 1
        temp = head
        while temp:
            if temp.random:
                random_indices.append(index_map[temp.random])
            else:
                random_indices.append(None)
            temp = temp.next
        return array, random_indices

    def test_copy_random_list_empty(self):
        """Test copying an empty list."""
        self.assertIsNone(CopyListWithRandomPointer.copyRandomList(None))

    def test_copy_random_list_single_node_no_random(self):
        """Test copying a list with a single node without random pointer."""
        node = ListNodeWithRandom(1)
        cloned_head = CopyListWithRandomPointer.copyRandomList(node)
        self.assertIsNotNone(cloned_head)
        self.assertEqual(cloned_head.val, 1)
        self.assertIsNone(cloned_head.next)
        self.assertIsNone(cloned_head.random)

    def test_copy_random_list_single_node_with_random(self):
        """Test copying a list with a single node with random pointer to itself."""
        node = ListNodeWithRandom(1)
        node.random = node
        cloned_head = CopyListWithRandomPointer.copyRandomList(node)
        self.assertIsNotNone(cloned_head)
        self.assertEqual(cloned_head.val, 1)
        self.assertIsNone(cloned_head.next)
        self.assertIsNotNone(cloned_head.random)
        self.assertEqual(cloned_head, cloned_head.random)

    def test_copy_random_list_multiple_nodes_no_random(self):
        """Test copying a list with multiple nodes and no random pointers."""
        node1 = ListNodeWithRandom(1)
        node2 = ListNodeWithRandom(2)
        node1.next = node2
        cloned_head = CopyListWithRandomPointer.copyRandomList(node1)
        self.assertIsNotNone(cloned_head)
        self.assertEqual(cloned_head.val, 1)
        self.assertIsNotNone(cloned_head.next)
        self.assertEqual(cloned_head.next.val, 2)
        self.assertIsNone(cloned_head.random)
        self.assertIsNone(cloned_head.next.random)

    def test_copy_random_list_multiple_nodes_with_random(self):
        """Test copying a list with multiple nodes and random pointers."""
        node1 = ListNodeWithRandom(1)
        node2 = ListNodeWithRandom(2)
        node3 = ListNodeWithRandom(3)
        node1.next = node2
        node2.next = node3
        node1.random = node3
        node2.random = node1
        node3.random = node2
        cloned_head = CopyListWithRandomPointer.copyRandomList(node1)
        self.assertIsNotNone(cloned_head)
        self.assertEqual(cloned_head.val, 1)
        self.assertIsNotNone(cloned_head.next)
        self.assertEqual(cloned_head.next.val, 2)
        self.assertIsNotNone(cloned_head.next.next)
        self.assertEqual(cloned_head.next.next.val, 3)
        self.assertIsNone(cloned_head.next.next.next)

        # Verify random pointers
        self.assertEqual(cloned_head.random.val, 3)
        self.assertEqual(cloned_head.next.random.val, 1)
        self.assertEqual(cloned_head.next.next.random.val, 2)


if __name__ == "__main__":
    unittest.main()
