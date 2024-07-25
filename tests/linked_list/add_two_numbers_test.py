import unittest
from typing import Optional

from problems.linked_list.add_two_numbers import AddTwoNumbers
from problems.util.list_node import ListNode


def list_to_array(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def array_to_list(array: list) -> Optional[ListNode]:
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for val in array[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class AddTwoNumbersTest(unittest.TestCase):

    def test_both_lists_empty(self):
        self.assertIsNone(AddTwoNumbers.addTwoNumbers(None, None))

    def test_first_list_empty(self):
        l2 = array_to_list([1, 2, 3])
        result = AddTwoNumbers.addTwoNumbers(None, l2)
        self.assertEqual(list_to_array(l2), list_to_array(result))

    def test_second_list_empty(self):
        l1 = array_to_list([1, 2, 3])
        result = AddTwoNumbers.addTwoNumbers(l1, None)
        self.assertEqual(list_to_array(l1), list_to_array(result))

    def test_same_length_no_carry(self):
        l1 = array_to_list([2, 4, 3])
        l2 = array_to_list([5, 6, 4])
        result = AddTwoNumbers.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_array(result), [7, 0, 8])

    def test_different_length(self):
        l1 = array_to_list([9, 9])
        l2 = array_to_list([1])
        result = AddTwoNumbers.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_array(result), [0, 0, 1])

        l1 = array_to_list([1])
        l2 = array_to_list([9, 9])
        result = AddTwoNumbers.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_array(result), [0, 0, 1])

    def test_with_carry(self):
        l1 = array_to_list([9, 9, 9])
        l2 = array_to_list([1])
        result = AddTwoNumbers.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_array(result), [0, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
