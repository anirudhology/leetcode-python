from typing import Optional

from problems.util.list_node import ListNode


class LinkedListCycle:
    @staticmethod
    def hasCycle(head: Optional[ListNode]) -> bool:
        # Special case
        if head is None:
            return False
        # Slow and fast pointers
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
