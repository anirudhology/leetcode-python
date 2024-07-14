class StackNode:
    def __init__(self, value: int, min_value: int, next_node: 'StackNode' = None):
        self.value = value
        self.min_value = min_value
        self.next = next_node
