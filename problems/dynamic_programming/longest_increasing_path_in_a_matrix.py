from typing import List


class LongestIncreasingPathInAMatrix:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        # Lookup table to store longest increasing path
        lookup = [[0] * n for _ in range(m)]
        # Longest path
        max_path = 1
        # Process for each cell
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, self.dfs(matrix, i, j, m, n, lookup))

        return max_path

    def dfs(self, matrix: List[List[int]], i: int, j: int, m: int, n: int, lookup: List[List[int]]):
        # If we have already calculated this result
        if lookup[i][j] != 0:
            return lookup[i][j]
        # Directions
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        # Longest path length
        longest_path = 1
        # DFS in four directions
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            # Check for boundary conditions
            if x < 0 or x >= m or y < 0 or y >= n:
                continue
            if matrix[x][y] <= matrix[i][j]:
                continue
            longest_path = max(longest_path, 1 + self.dfs(matrix, x, y, m, n, lookup))
        lookup[i][j] = longest_path
        return longest_path
