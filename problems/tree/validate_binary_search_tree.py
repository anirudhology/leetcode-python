from typing import Optional

from problems.util.tree_node import TreeNode


class ValidateBinarySearchTree:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root: Optional[TreeNode], min_value: float, max_value: float):
        # Base case
        if root is None:
            return True
        if root.val >= max_value or root.val <= min_value:
            return False
        return self.dfs(root.left, min_value, root.val) and self.dfs(root.right, root.val, max_value)
