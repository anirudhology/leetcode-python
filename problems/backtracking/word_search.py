from typing import List


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Special case
        if board is None or len(board) == 0 or word is None or len(word) == 0:
            return False
        # Dimensions of the board
        m, n = len(board), len(board[0])
        # Process the elements on the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.search(board, i, j, m, n, word, 0):
                    return True
        return False

    def search(
            self,
            board: List[List[str]],
            i: int,
            j: int,
            m: int,
            n: int,
            word: str,
            index: int,
    ):
        # Base case
        if index == len(word):
            return True
        # Check for out of bound indices
        if i >= m or i < 0 or j >= n or j < 0 or board[i][j] != word[index]:
            return False
        if board[i][j] == "#":
            return False
        temp = board[i][j]
        board[i][j] = "#"
        found = (
                self.search(board, i - 1, j, m, n, word, index + 1)
                or self.search(board, i + 1, j, m, n, word, index + 1)
                or self.search(board, i, j - 1, m, n, word, index + 1)
                or self.search(board, i, j + 1, m, n, word, index + 1)
        )
        board[i][j] = temp
        return found
