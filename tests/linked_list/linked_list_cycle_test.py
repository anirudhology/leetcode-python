import unittest

from problems.linked_list.linked_list_cycle import LinkedListCycle
from problems.util.list_node import ListNode


class LinkedListCycleTest(unittest.TestCase):

    def test_has_cycle_empty_list(self):
        self.assertFalse(LinkedListCycle.hasCycle(None))

    def test_has_cycle_single_element_no_cycle(self):
        head = ListNode(1)
        self.assertFalse(LinkedListCycle.hasCycle(head))

    def test_has_cycle_multiple_elements_no_cycle(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertFalse(LinkedListCycle.hasCycle(head))

    def test_has_cycle_multiple_elements_with_cycle(self):
        head = ListNode(1)
        second = ListNode(2)
        third = ListNode(3)
        head.next = second
        second.next = third
        third.next = second  # Creating a cycle
        self.assertTrue(LinkedListCycle.hasCycle(head))

    def test_has_cycle_cycle_at_head(self):
        head = ListNode(1)
        second = ListNode(2)
        head.next = second
        second.next = head  # Creating a cycle at the head
        self.assertTrue(LinkedListCycle.hasCycle(head))

    def test_has_cycle_cycle_at_middle(self):
        head = ListNode(1)
        second = ListNode(2)
        third = ListNode(3)
        fourth = ListNode(4)
        head.next = second
        second.next = third
        third.next = fourth
        fourth.next = second  # Creating a cycle at the second node
        self.assertTrue(LinkedListCycle.hasCycle(head))


if __name__ == '__main__':
    unittest.main()
