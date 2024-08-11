from typing import List


class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Special case
        if grid is None or len(grid) == 0:
            return 0
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        # Total number of islands
        count = 0
        # Process every cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, m, n)
                    count += 1
        return count

    def dfs(self, grid: List[List[str]], i: int, j: int, m: int, n: int):
        # Base case
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        # Perform DFS
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i, j - 1, m, n)
        self.dfs(grid, i, j + 1, m, n)
