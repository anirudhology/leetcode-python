from typing import Optional

from problems.util.list_node import ListNode


class MergeTwoSortedLists:
    @staticmethod
    def mergeTwoLists(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        # Special cases
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        # Head of the resultant list
        if head1.val < head2.val:
            head = ListNode(head1.val)
            head1 = head1.next
        else:
            head = ListNode(head2.val)
            head2 = head2.next
        # Pointer to traverse through the resultant list
        temp = head
        # Process both lists together
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                temp.next = ListNode(head1.val)
                head1 = head1.next
            else:
                temp.next = ListNode(head2.val)
                head2 = head2.next
            temp = temp.next
        # Process remaining nodes in lists
        while head1 is not None:
            temp.next = ListNode(head1.val)
            head1 = head1.next
            temp = temp.next
        while head2 is not None:
            temp.next = ListNode(head2.val)
            head2 = head2.next
            temp = temp.next
        return head
