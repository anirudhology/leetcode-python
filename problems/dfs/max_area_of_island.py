from typing import List


class MaxAreaOfIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Special case
        if grid is None or len(grid) == 0:
            return 0
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        # Array to mark the visited cells
        visited = [[False for _ in range(n)] for _ in range(m)]
        # Maximum area
        max_area = 0
        # Process every cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    current_area = self.dfs(grid, i, j, m, n, visited)
                    max_area = max(max_area, current_area)
        return max_area

    def dfs(
            self,
            grid: List[List[int]],
            i: int,
            j: int,
            m: int,
            n: int,
            visited: List[List[bool]],
    ) -> int:
        # Base case
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
            return 0
        # Mark the current cell as visited
        visited[i][j] = True
        if grid[i][j] == 0:
            return 0
        # Perform DFS
        return (
                1
                + self.dfs(grid, i - 1, j, m, n, visited)
                + self.dfs(grid, i + 1, j, m, n, visited)
                + self.dfs(grid, i, j - 1, m, n, visited)
                + self.dfs(grid, i, j + 1, m, n, visited)
        )
