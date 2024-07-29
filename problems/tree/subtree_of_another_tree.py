from typing import Optional

from problems.util.tree_node import TreeNode


class SubtreeOfAnotherTree:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.is_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None or s.val != t.val:
            return False
        return self.is_same(s.left, t.left) and self.is_same(s.right, t.right)
