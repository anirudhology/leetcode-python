import unittest
from typing import Optional

from problems.linked_list.remove_nth_node_from_end_of_list import RemoveNthNodeFromEndOfList
from problems.util.list_node import ListNode


class RemoveNthNodeFromEndOfListTest(unittest.TestCase):

    @staticmethod
    def list_to_array(head: Optional[ListNode]) -> list:
        array = []
        current = head
        while current is not None:
            array.append(current.val)
            current = current.next
        return array

    @staticmethod
    def array_to_list(array: list) -> Optional[ListNode]:
        if not array:
            return None
        head = ListNode(array[0])
        current = head
        for val in array[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def test_removeNthFromEnd_empty_list(self):
        remove_nth_node = RemoveNthNodeFromEndOfList()
        head = None
        n = 1
        result = remove_nth_node.removeNthFromEnd(head, n)
        self.assertIsNone(result)

    def test_removeNthFromEnd_single_node(self):
        remove_nth_node = RemoveNthNodeFromEndOfList()
        head = ListNode(1)
        n = 1
        result = remove_nth_node.removeNthFromEnd(head, n)
        self.assertIsNone(result)

    def test_removeNthFromEnd_remove_first_node(self):
        remove_nth_node = RemoveNthNodeFromEndOfList()
        head = self.array_to_list([1, 2, 3])
        n = 3
        result = remove_nth_node.removeNthFromEnd(head, n)
        expected = [2, 3]
        self.assertEqual(self.list_to_array(result), expected)

    def test_removeNthFromEnd_remove_last_node(self):
        remove_nth_node = RemoveNthNodeFromEndOfList()
        head = self.array_to_list([1, 2, 3])
        n = 1
        result = remove_nth_node.removeNthFromEnd(head, n)
        expected = [1, 2]
        self.assertEqual(self.list_to_array(result), expected)

    def test_removeNthFromEnd_middle_node(self):
        remove_nth_node = RemoveNthNodeFromEndOfList()
        head = self.array_to_list([1, 2, 3, 4])
        n = 2
        result = remove_nth_node.removeNthFromEnd(head, n)
        expected = [1, 2, 4]
        self.assertEqual(self.list_to_array(result), expected)


if __name__ == "__main__":
    unittest.main()
