from typing import Optional

from problems.util.tree_node import TreeNode


class BinaryTreeMaximumPathSum:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> float:
        self.helper(root)
        return self.max_sum

    def helper(self, root: Optional[TreeNode]) -> int:
        # Base case
        if root is None:
            return 0
        # Find sum of left and right subtree that give non-negative outcome
        left_sum = max(self.helper(root.left), 0)
        right_sum = max(self.helper(root.right), 0)
        # Total sum for the current node
        current_sum = root.val + left_sum + right_sum
        # Update max_sum if required
        self.max_sum = max(current_sum, self.max_sum)
        # Pick the largest path
        return root.val + max(left_sum, right_sum)
