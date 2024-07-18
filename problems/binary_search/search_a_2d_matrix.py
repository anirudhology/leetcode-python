from typing import List


class SearchA2DMatrix:
    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        # Special case
        if matrix is None or len(matrix) == 0:
            return False
        # Dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        # Start and end pointers
        start, end = 0, m * n - 1
        # Search in the given space
        while start <= end:
            middle = start + (end - start) // 2
            i, j = middle // n, middle % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                start = middle + 1
            else:
                end = middle - 1
        return False
