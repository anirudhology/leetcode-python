from typing import Optional

from problems.util.tree_node import TreeNode


class KthSmallestElementInABST:

    def __init__(self):
        self.kth_smallest_element = 0
        self.count = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.find_kth_smallest_element(root)
        return self.kth_smallest_element

    def find_kth_smallest_element(self, root: Optional[TreeNode]):
        # Base case
        if root is None:
            return
        # Move towards left subtree first
        if root.left is not None:
            self.find_kth_smallest_element(root.left)
        self.count -= 1
        # Check if we have found the kth smallest element
        if self.count == 0:
            self.kth_smallest_element = root.val
        # If we have not found required element yet, check in the right subtree
        if root.right is not None:
            self.find_kth_smallest_element(root.right)
