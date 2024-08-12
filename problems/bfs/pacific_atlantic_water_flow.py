from collections import deque
from typing import List


class PacificAtlanticWaterFlow:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # List to store the coordinates
        coordinates = []
        # Special case
        if heights is None or len(heights) == 0:
            return coordinates
        # Dimensions of the island
        m, n = len(heights), len(heights[0])
        # Queues to perform BFS for both oceans
        pacific_cells = deque([])
        atlantic_cells = deque([])
        # Boolean arrays to mark visited cells
        pacific_visited = [[False for _ in range(n)] for _ in range(m)]
        atlantic_visited = [[False for _ in range(n)] for _ in range(m)]
        # Populate the queues and arrays
        for i in range(m):
            pacific_cells.append([i, 0])
            atlantic_cells.append([i, n - 1])
            pacific_visited[i][0] = True
            atlantic_visited[i][n - 1] = True
        for j in range(n):
            pacific_cells.append([0, j])
            atlantic_cells.append([m - 1, j])
            pacific_visited[0][j] = True
            atlantic_visited[m - 1][j] = True
        # Perform BFS on both oceans
        self.bfs(heights, pacific_cells, pacific_visited, m, n)
        self.bfs(heights, atlantic_cells, atlantic_visited, m, n)
        # Populate the result
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    coordinates.append([i, j])
        return coordinates

    @staticmethod
    def bfs(heights: List[List[int]], cells: deque, visited: List[List[int]], m: int, n: int):
        # Four directions
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while cells:
            cell = cells.popleft()
            # Check in all four directions
            for direction in directions:
                x = direction[0] + cell[0]
                y = direction[1] + cell[1]
                if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or heights[x][y] < heights[cell[0]][cell[1]]:
                    continue
                cells.append([x, y])
                visited[x][y] = True
