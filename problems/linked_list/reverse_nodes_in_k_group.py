from typing import Optional

from problems.util.list_node import ListNode


class ReverseNodesInKGroup:
    @staticmethod
    def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Special case
        if head is None or k <= 0:
            return head
        # Dummy head
        dummy = ListNode()
        dummy.next = head
        # Pointer to traverse the list
        temp = dummy
        # Traverse the list
        while True:
            current_temp = temp
            # Check if we have k nodes to reverse
            index = 0
            while index < k and current_temp is not None:
                current_temp = current_temp.next
                index += 1
            if current_temp is None:
                break
            # Reverse the list
            previous_node, current_node, next_node = None, temp.next, None
            for i in range(k):
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            # Tail of the group
            tail = temp.next
            tail.next = current_node
            temp.next = previous_node
            temp = tail
        return dummy.next
