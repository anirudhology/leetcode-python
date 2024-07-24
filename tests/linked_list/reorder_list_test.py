import unittest

from problems.linked_list.reorder_list import ReorderList
from problems.util.list_node import ListNode


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class ReorderListTest(unittest.TestCase):
    def setUp(self):
        self.reorder_list = ReorderList()

    def test_empty_list(self):
        head = None
        self.reorder_list.reorderList(head)
        self.assertIsNone(head)

    def test_single_element_list(self):
        head = build_list([1])
        self.reorder_list.reorderList(head)
        self.assertEqual(list_to_array(head), [1])

    def test_two_element_list(self):
        head = build_list([1, 2])
        self.reorder_list.reorderList(head)
        self.assertEqual(list_to_array(head), [1, 2])

    def test_three_element_list(self):
        head = build_list([1, 2, 3])
        self.reorder_list.reorderList(head)
        self.assertEqual(list_to_array(head), [1, 3, 2])

    def test_four_element_list(self):
        head = build_list([1, 2, 3, 4])
        self.reorder_list.reorderList(head)
        self.assertEqual(list_to_array(head), [1, 4, 2, 3])

    def test_odd_number_of_elements(self):
        head = build_list([1, 2, 3, 4, 5])
        self.reorder_list.reorderList(head)
        self.assertEqual(list_to_array(head), [1, 5, 2, 4, 3])

    def test_even_number_of_elements(self):
        head = build_list([1, 2, 3, 4, 5, 6])
        self.reorder_list.reorderList(head)
        self.assertEqual(list_to_array(head), [1, 6, 2, 5, 3, 4])

    def test_get_middle(self):
        head = build_list([1, 2, 3, 4, 5])
        middle = self.reorder_list.get_middle(head)
        self.assertEqual(middle.val, 3)

    def test_reverse_list(self):
        head = build_list([1, 2, 3, 4, 5])
        reversed_head = self.reorder_list.reverse(head)
        self.assertEqual(list_to_array(reversed_head), [5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
