from problems.util.tree_node import TreeNode


class LowestCommonAncestorOfABinarySearchTree:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode | None:
        # Special case
        if root is None or p is None or q is None:
            return None
        if root.val > p.val and root.val > q.val:
            # If value of root is greater than values at both p and q,
            # it means LCA can only be in the left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            # If value of root is smaller than values at both p and q,
            # it means LCA can only be in the right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # We will reach here if value is root is in between values at
            # p and q. If this happens, then only root can be the LCA
            return root
