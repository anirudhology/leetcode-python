from typing import List


class SetMatrixZeroes:
    @staticmethod
    def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
        # Special case
        if not matrix:
            return matrix
        # Dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        # Flags to denote if first row and first column contain zero
        first_row, first_column = False, False
        # Traverse the matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_column = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Traverse the matrix except first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Process if firs row and column are true
        if first_row:
            for j in range(0, n):
                matrix[0][j] = 0
        if first_column:
            for i in range(0, m):
                matrix[i][0] = 0
        return matrix
