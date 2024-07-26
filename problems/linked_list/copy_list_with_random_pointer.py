from typing import Optional

from problems.util.list_node_with_random import ListNodeWithRandom


class CopyListWithRandomPointer:
    @staticmethod
    def copyRandomList(head: 'Optional[ListNodeWithRandom]') -> 'Optional[ListNodeWithRandom]':
        # Special case
        if head is None:
            return None
        # Dictionary to store the mappings of original and clone list
        mappings = {}
        # Head of the cloned list
        clone = None
        # Pointers to traverse the list
        temp, clone_temp = head, None
        # Traverse the list
        while temp is not None:
            # Create a cloned node
            copy = ListNodeWithRandom(temp.val)
            if clone is None:
                clone = copy
                clone_temp = clone
            else:
                clone_temp.next = copy
                clone_temp = clone_temp.next
            # Add the mapping
            mappings[temp] = clone_temp
            temp = temp.next
        # Reset temp pointers
        temp, clone_temp = head, clone
        while temp is not None:
            if temp.random is not None:
                clone_temp.random = mappings[temp.random]
            temp = temp.next
            clone_temp = clone_temp.next
        return clone
