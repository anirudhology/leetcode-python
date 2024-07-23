from typing import Optional
from problems.util.list_node import ListNode


class ReverseLinkedList:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        # Special case
        if head is None or head.next is None:
            return head
        # Three pointers to traverse linked list
        previous_node, current_node, next_node = None, head, None
        # Traverse through the list
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node
