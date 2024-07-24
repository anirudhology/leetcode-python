from typing import Optional

from problems.util.list_node import ListNode


class ReorderList:
    def reorderList(self, head: Optional[ListNode]) -> ListNode | None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Special case
        if head is None or head.next is None:
            return head
        # Find the middle of the list
        middle = self.get_middle(head)
        # Divide the list in two halves
        head_1, head_2 = head, middle.next
        middle.next = None
        # Find the reverse of the second half
        reverse_head_2 = self.reverse(head_2)
        # Merge two lists
        while head_1 is not None and reverse_head_2 is not None:
            next_1, next_2 = head_1.next, reverse_head_2.next
            head_1.next = reverse_head_2
            reverse_head_2.next = next_1
            head_1 = next_1
            reverse_head_2 = next_2
        return head

    @staticmethod
    def get_middle(head: Optional[ListNode]) -> ListNode:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def reverse(head: Optional[ListNode]) -> ListNode:
        previous_node, current_node, next_node = None, head, None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node
