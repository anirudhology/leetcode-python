from typing import List


class NQueens:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # List to store the combinations
        combinations = []
        # Special case
        if n == 0:
            return combinations
        # Create a board for n-queens
        board = [['.' for _ in range(n)] for _ in range(n)]
        # Perform backtracking
        self.backtrack(board, 0, combinations)
        return combinations

    def backtrack(self, board: List[List[str]], index: int, combinations: List[List[str]]):
        # Base case
        if index == len(board):
            combinations.append(self.build(board))
            return
        for i in range(len(board)):
            if self.check(board, i, index):
                board[i][index] = 'Q'
                self.backtrack(board, index + 1, combinations)
                board[i][index] = '.'

    @staticmethod
    def check(board: List[List[str]], row: int, column: int):
        for i in range(len(board)):
            for j in range(column):
                if board[i][j] == 'Q' and (row + j == column + i or row + column == i + j or row == i):
                    return False
        return True

    @staticmethod
    def build(board: List[List[str]]):
        combination = []
        for i in range(len(board)):
            s = ''
            for j in range(len(board)):
                s += board[i][j]
            combination.append(s)
        return combination
