from collections import deque

from problems.util.tree_node import TreeNode


class SerializeAndDeserializeBinaryTree:
    class Codec:

        @staticmethod
        def serialize(root):
            """Encodes a tree to a single string.

            :type root: TreeNode
            :rtype: str
            """
            if root is None:
                return ""
            # String to store the nodes in serialized format
            serialized = ""
            # Perform BFS on the tree
            nodes = deque([root])
            # Process all nodes in the tree
            while len(nodes) > 0:
                # Get front of the queue
                node = nodes.popleft()
                if node is None:
                    serialized += "n"
                else:
                    serialized += str(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
            return " ".join(serialized)

        @staticmethod
        def deserialize(data):
            """Decodes your encoded data to tree.

            :type data: str
            :rtype: TreeNode
            """
            # Base case
            if data == "":
                return None
            # Get all values for nodes
            values = data.split()
            # Create root of the tree
            root = TreeNode(values[0])
            # Queue for BFS
            nodes = deque([root])
            # Process remaining values
            for i in range(1, len(values), 2):
                # Get node from the front of the queue
                node = nodes.popleft()
                if node is not None:
                    if values[i] != "n":
                        node.left = TreeNode(int(values[i]))
                        nodes.append(node.left)
                    if values[i + 1] != "n":
                        node.right = TreeNode(int(values[i + 1]))
                        nodes.append(node.right)
            return root
