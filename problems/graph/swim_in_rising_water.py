import heapq
from typing import List


class SwimInRisingWater:
    @staticmethod
    def swimInWater(grid: List[List[int]]) -> int:
        # Dimensions of the grid
        n = len(grid)
        # Min heap to store the cells based on the lowest value
        min_heap = [(grid[0][0], 0, 0)]
        # Array to mark the visited cells
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        # Directions
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Loop until heap is empty
        while min_heap:
            time, i, j = heapq.heappop(min_heap)
            # Check if we have reached the last cell
            if i == n - 1 and j == n - 1:
                return time
            # Move in all four directions
            for direction in directions:
                x, y = i + direction[0], j + direction[1]
                # Check for out of bounds
                if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
                    continue
                visited[x][y] = True
                heapq.heappush(min_heap, (max(grid[x][y], time), x, y))
        return -1
