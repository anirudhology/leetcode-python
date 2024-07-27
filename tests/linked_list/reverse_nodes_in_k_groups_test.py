import unittest

from problems.linked_list.reverse_nodes_in_k_group import ReverseNodesInKGroup
from problems.util.list_node import ListNode


class ReverseNodesInKGroupTest(unittest.TestCase):

    @staticmethod
    def create_list(values):
        dummy = ListNode()
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    @staticmethod
    def list_to_array(head):
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def test_reverseKGroup_with_null_head(self):
        result = ReverseNodesInKGroup.reverseKGroup(None, 3)
        self.assertIsNone(result)

    def test_reverseKGroup_with_k_less_than_or_equal_to_zero(self):
        head = self.create_list([1, 2, 3])
        result = ReverseNodesInKGroup.reverseKGroup(head, 0)
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_reverseKGroup_with_single_element(self):
        head = self.create_list([1])
        result = ReverseNodesInKGroup.reverseKGroup(head, 1)
        self.assertEqual(self.list_to_array(result), [1])

    def test_reverseKGroup_with_k_greater_than_list_length(self):
        head = self.create_list([1, 2, 3])
        result = ReverseNodesInKGroup.reverseKGroup(head, 4)
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_reverseKGroup_with_k_equals_list_length(self):
        head = self.create_list([1, 2, 3])
        result = ReverseNodesInKGroup.reverseKGroup(head, 3)
        self.assertEqual(self.list_to_array(result), [3, 2, 1])

    def test_reverseKGroup_with_multiple_k_groups(self):
        head = self.create_list([1, 2, 3, 4, 5])
        result = ReverseNodesInKGroup.reverseKGroup(head, 2)
        self.assertEqual(self.list_to_array(result), [2, 1, 4, 3, 5])

    def test_reverseKGroup_with_remaining_nodes_less_than_k(self):
        head = self.create_list([1, 2, 3, 4, 5])
        result = ReverseNodesInKGroup.reverseKGroup(head, 3)
        self.assertEqual(self.list_to_array(result), [3, 2, 1, 4, 5])


if __name__ == '__main__':
    unittest.main()
