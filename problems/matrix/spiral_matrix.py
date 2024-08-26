from typing import List


class SpiralMatrix:
    @staticmethod
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        # List to store final spiral order
        spiral = []
        # Special case
        if not matrix:
            return spiral
        # Dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        # Variables to keep track of boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
        # Process all elements in the matrix
        while top <= bottom and left <= right:
            # Move from left to right
            for i in range(left, right + 1):
                spiral.append(matrix[top][i])
            top += 1
            # Move from top to bottom
            for i in range(top, bottom + 1):
                spiral.append(matrix[i][right])
            right -= 1
            # Check if we are out of bounds
            if left > right or top > bottom:
                break
            # Move from right to left
            for i in range(right, left - 1, -1):
                spiral.append(matrix[bottom][i])
            bottom -= 1
            # Move from bottom to top
            for i in range(bottom, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1
        return spiral
