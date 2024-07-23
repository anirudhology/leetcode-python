import unittest

from problems.linked_list.merge_two_sorted_lists import MergeTwoSortedLists
from problems.util.list_node import ListNode


class MergeTwoListsTest(unittest.TestCase):
    def test_merge_two_lists(self):
        list1 = ListNode(1, ListNode(3, ListNode(5)))
        list2 = ListNode(2, ListNode(4, ListNode(6)))
        merged_list = MergeTwoSortedLists.mergeTwoLists(list1, list2)

        self.assertEqual(merged_list.val, 1)
        self.assertEqual(merged_list.next.val, 2)
        self.assertEqual(merged_list.next.next.val, 3)
        self.assertEqual(merged_list.next.next.next.val, 4)
        self.assertEqual(merged_list.next.next.next.next.val, 5)
        self.assertEqual(merged_list.next.next.next.next.next.val, 6)

    def test_merge_with_null_list(self):
        list1 = None
        list2 = ListNode(1, ListNode(2, ListNode(3)))
        merged_list = MergeTwoSortedLists.mergeTwoLists(list1, list2)

        self.assertEqual(merged_list.val, 1)
        self.assertEqual(merged_list.next.val, 2)
        self.assertEqual(merged_list.next.next.val, 3)

    def test_merge_both_null(self):
        list1 = None
        list2 = None
        merged_list = MergeTwoSortedLists.mergeTwoLists(list1, list2)
        self.assertIsNone(merged_list)


if __name__ == '__main__':
    unittest.main()
