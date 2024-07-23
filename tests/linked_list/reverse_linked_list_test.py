import unittest
from problems.linked_list.reverse_linked_list import ReverseLinkedList
from problems.util.list_node import ListNode


class ReverseLinkedListTest(unittest.TestCase):

    def test_reverse_empty_list(self):
        reverse_linked_list = ReverseLinkedList()
        head = None
        result = reverse_linked_list.reverseList(head)
        self.assertIsNone(result)

    def test_reverse_single_element_list(self):
        reverse_linked_list = ReverseLinkedList()
        head = ListNode(1)
        result = reverse_linked_list.reverseList(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)

    def test_reverse_multiple_element_list(self):
        reverse_linked_list = ReverseLinkedList()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        result = reverse_linked_list.reverseList(head)

        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)
        self.assertIsNotNone(result.next)
        self.assertEqual(result.next.val, 2)
        self.assertIsNotNone(result.next.next)
        self.assertEqual(result.next.next.val, 1)
        self.assertIsNone(result.next.next.next)

    def test_reverse_two_element_list(self):
        reverse_linked_list = ReverseLinkedList()
        head = ListNode(1)
        head.next = ListNode(2)

        result = reverse_linked_list.reverseList(head)

        self.assertIsNotNone(result)
        self.assertEqual(result.val, 2)
        self.assertIsNotNone(result.next)
        self.assertEqual(result.next.val, 1)
        self.assertIsNone(result.next.next)


if __name__ == '__main__':
    unittest.main()
