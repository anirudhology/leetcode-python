from collections import deque
from typing import List


class WallsAndGates:
    @staticmethod
    def islandsAndTreasure(rooms: List[List[int]]) -> list[list[int]] | None:
        # Special case
        if rooms is None or len(rooms) == 0:
            return rooms
        # Dimensions of rooms
        m, n = len(rooms), len(rooms[0])
        # Queue to perform BFS
        cells = deque([])
        # Mark all the cells with gates
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    cells.append([i, j])
        # Distance of cells from gates
        distance = 0
        # Four directions
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while cells:
            distance += 1
            for i in range(len(cells)):
                # Get front of the queue
                cell = cells.popleft()
                # Check in four directions w.r.t. this cell
                for direction in directions:
                    x = direction[0] + cell[0]
                    y = direction[1] + cell[1]
                    # Check if x and y are valid coordinates
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == float('inf'):
                        rooms[x][y] = distance
                        cells.append([x, y])
        return rooms
