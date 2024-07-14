from problems.util.stack_node import StackNode


class MinStack:

    def __init__(self):
        # Head of the stack
        self.head = None

    def push(self, val: int) -> None:
        # If this is the very first node
        if self.head is None:
            self.head = StackNode(val, val, None)
        # For subsequent nodes
        else:
            self.head = StackNode(val, min(val, self.head.min_value), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.head.min_value
