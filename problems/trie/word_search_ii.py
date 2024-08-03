from typing import List

from problems.util.trie_node_with_word import TrieNodeWithWord


class WordSearchII:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # List to store the final output
        result = []
        # Special case
        if board is None or len(board) == 0 or words is None or len(words) == 0:
            return result
        # Build trie
        root = self.build_trie(words)
        # Dimensions of the board
        m, n = len(board), len(board[0])
        # Process every cell in the board
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, m, n, root, result)
        return result

    @staticmethod
    def build_trie(words) -> TrieNodeWithWord:
        root = TrieNodeWithWord()
        for word in words:
            current = root
            for c in word:
                if not current.children[ord(c) - ord('a')]:
                    current.children[ord(c) - ord('a')] = TrieNodeWithWord()
                current = current.children[ord(c) - ord('a')]
            current.word = word
        return root

    def dfs(self, board: List[List[str]], i: int, j: int, m: int, n: int, node: TrieNodeWithWord,
            result: List[str]):
        # Handle out of bound indices
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        c = board[i][j]
        # If we have already visited this cell
        if c == '#':
            return
        if not node.children[ord(c) - ord('a')]:
            return
        node = node.children[ord(c) - ord('a')]
        if node.word is not None:
            result.append(node.word)
            node.word = None
        board[i][j] = '#'
        self.dfs(board, i - 1, j, m, n, node, result)
        self.dfs(board, i + 1, j, m, n, node, result)
        self.dfs(board, i, j - 1, m, n, node, result)
        self.dfs(board, i, j + 1, m, n, node, result)
        board[i][j] = c
