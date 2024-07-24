from typing import Optional

from problems.util.list_node import ListNode


class RemoveNthNodeFromEndOfList:
    @staticmethod
    def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Slow and fast pointers
        slow, fast = head, head
        # Move fast pointer n steps ahead
        while n > 0 and fast is not None:
            fast = fast.next
            n -= 1
        # If fast is None, it means n >= number of nodes in the list
        if fast is None and head is not None:
            return head.next
        # Move both pointers at the same pace
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
        if slow is not None and slow.next is not None:
            slow.next = slow.next.next
        return head
