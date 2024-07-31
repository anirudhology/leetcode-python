from problems.util.tree_node import TreeNode


class CountGoodNodesInBinaryTree:

    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        # Perform DFS
        self.dfs(root, root.val)
        return self.count

    def dfs(self, node: TreeNode, max_value: int):
        if node is None:
            return
        # Perform preorder traversal
        if node.val >= max_value:
            self.count += 1
            max_value = node.val
        self.dfs(node.left, max_value)
        self.dfs(node.right, max_value)
