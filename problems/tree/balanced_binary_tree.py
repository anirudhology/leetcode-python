from typing import Optional

from problems.util.tree_node import TreeNode


class BalancedBinaryTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Find the heights of subtrees from bottom up manner
        return self.dfs(root) != -1

    def dfs(self, root: Optional[TreeNode]) -> int:
        # Base case
        if root is None:
            return 0
        # Height of the left subtree
        left = self.dfs(root.left)
        if left == -1:
            return -1
        # Height of the right subtree
        right = self.dfs(root.right)
        if right == -1:
            return -1
        # Check for the balancing property
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
