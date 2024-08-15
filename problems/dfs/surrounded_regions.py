from typing import List


class SurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        # Special case
        if board is None or len(board) == 0:
            return board
        # Dimensions of the board
        m, n = len(board), len(board[0])
        # Process the cells with 'O' at the boundary
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    self._boundary_dfs(board, i, j, m, n)

        # Post-processing
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'

        return board

    def _boundary_dfs(self, board: List[List[str]], i: int, j: int, m: int, n: int):
        # Check for valid cells
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        # Mark the boundary cell
        board[i][j] = '#'
        # Perform DFS in all four directions
        self._boundary_dfs(board, i - 1, j, m, n)
        self._boundary_dfs(board, i + 1, j, m, n)
        self._boundary_dfs(board, i, j - 1, m, n)
        self._boundary_dfs(board, i, j + 1, m, n)
