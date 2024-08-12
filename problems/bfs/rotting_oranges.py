from collections import deque
from typing import List


class RottingOranges:
    @staticmethod
    def orangesRotting(grid: List[List[int]]) -> int:
        # Special case
        if grid is None or len(grid) == 0:
            return 0
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        # Queue to perform BFS
        cells = deque([])
        # Total number of fresh oranges
        fresh_oranges = 0
        # Populate the queue with rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    cells.append([i, j])
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        # If there are no fresh oranges
        if fresh_oranges == 0:
            return 0
        # Minutes required to make all oranges rotten
        minutes = 0
        # Four directions
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        # Process all rotten oranges
        while cells:
            minutes += 1
            size = len(cells)
            for _ in range(size):
                cell = cells.popleft()
                # For all four directions
                for direction in directions:
                    x = direction[0] + cell[0]
                    y = direction[1] + cell[1]
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                        continue
                    grid[x][y] = 2
                    cells.append([x, y])
                    fresh_oranges -= 1
        return -1 if fresh_oranges != 0 else minutes - 1
