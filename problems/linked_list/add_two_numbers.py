from typing import Optional

from problems.util.list_node import ListNode


class AddTwoNumbers:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Special case
        if l1 is None and l2 is None:
            return None
        # Dummy head of the resultant list
        dummy = ListNode()
        # Pointer to traverse the resultant list
        temp = dummy
        # Carry
        carry = 0
        # Traverse through both lists together
        while l1 is not None and l2 is not None:
            sum_value = carry + l1.val + l2.val
            carry = sum_value // 10
            temp.next = ListNode(sum_value % 10)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        # Process remaining nodes
        while l1 is not None:
            sum_value = carry + l1.val
            carry = sum_value // 10
            temp.next = ListNode(sum_value % 10)
            temp = temp.next
            l1 = l1.next
        while l2 is not None:
            sum_value = carry + l2.val
            carry = sum_value // 10
            temp.next = ListNode(sum_value % 10)
            temp = temp.next
            l2 = l2.next
        # Adjust remaining carry, if any
        if carry != 0:
            temp.next = ListNode(carry)
        return dummy.next
