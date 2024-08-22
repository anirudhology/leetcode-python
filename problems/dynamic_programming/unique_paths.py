class UniquePaths:
    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        # Lookup table to store unique paths count for a cell {i, j}
        lookup = [[0 for _ in range(n)] for _ in range(m)]
        # For the first row, we can only move horizontally
        for j in range(n):
            lookup[0][j] = 1
        # For the first column, we can only move vertically
        for i in range(m):
            lookup[i][0] = 1
        # Populate remaining cells
        for i in range(1, m):
            for j in range(1, n):
                lookup[i][j] = lookup[i - 1][j] + lookup[i][j - 1]
        return lookup[m - 1][n - 1]
