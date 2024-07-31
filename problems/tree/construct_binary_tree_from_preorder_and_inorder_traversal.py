from typing import List, Optional

from problems.util.tree_node import TreeNode


class ConstructBinaryTreeFromPreorderAndInorderTraversal:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Dictionary to store indices of elements in the inorder array
        index_mappings = {}
        for i in range(len(inorder)):
            index_mappings[inorder[i]] = i
        # Perform DFS traversal on the tree
        return self.helper(0, len(preorder) - 1, 0, len(inorder) - 1, preorder, inorder, index_mappings)

    def helper(self, pre_start, pre_end, in_start, in_end, preorder, inorder, index_mappings):
        # Base case
        if pre_start > pre_end or in_start > in_end:
            return None
        # Create a tree node with the element at pre_start
        root = TreeNode(preorder[pre_start])
        # Get the index of this element in inorder
        index = index_mappings[root.val]
        # Now, all the elements to the left of the current index in the inorder
        # array will lie in the left subtree and all the elements to the right
        # of the current index in the inorder array will lie in the right subtree
        root.left = self.helper(pre_start + 1, pre_end, in_start, index - 1, preorder, inorder, index_mappings)
        root.right = self.helper(pre_start + index - in_start + 1, pre_end, index + 1, in_end, preorder, inorder,
                                 index_mappings)
        return root
