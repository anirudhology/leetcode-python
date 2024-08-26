from typing import List


class RotateImage:
    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        # Order of the matrix
        n = len(matrix)
        # Left and right pointers
        left, right = 0, n - 1
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
