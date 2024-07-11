from typing import List


class ValidSudoku:
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        # Set to store the encodings of elements on the sudoku board
        encodings = set()
        # Process the board one cell at a time
        for i in range(9):
            for j in range(9):
                # Current number
                c = board[i][j]
                # Process only already present elements
                if c != '.':
                    row_string = f"{c} is present in row: {i}"
                    column_string = f"{c} is present in column: {j}"
                    block_string = f"{c} is present in block: {i // 3}-{j // 3}"
                    if (row_string in encodings) or (column_string in encodings) or (block_string in encodings):
                        return False
                    encodings.add(row_string)
                    encodings.add(column_string)
                    encodings.add(block_string)
        return True
