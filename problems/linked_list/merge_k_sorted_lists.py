from typing import Optional, List

from problems.util.list_node import ListNode


class MergeKSortedLists:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Special case
        if lists is None or len(lists) == 0:
            return None
        return self.merge_lists(lists, 0, len(lists) - 1)

    def merge_lists(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        # Base case
        if left >= right:
            return lists[left]
        # Divide the list in two halves
        middle = left + (right - left) // 2
        left_half = self.merge_lists(lists, left, middle)
        right_half = self.merge_lists(lists, middle + 1, right)
        # Merge lists
        return self.merge(left_half, right_half)

    @staticmethod
    def merge(left: ListNode, right: ListNode) -> Optional[ListNode]:
        # Dummy head
        dummy = ListNode()
        # Pointer to traverse
        temp = dummy
        # Process both nodes
        while left is not None and right is not None:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        # Process remaining nodes
        while left is not None:
            temp.next = left
            left = left.next
            temp = temp.next
        while right is not None:
            temp.next = right
            right = right.next
            temp = temp.next
        return dummy.next
