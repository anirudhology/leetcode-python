from typing import List


class MinCostClimbingStairs:
    @staticmethod
    def minCostClimbingStairs(cost: List[int]) -> int:
        # Total number of  stairs
        n = len(cost)
        # Cost for climbing first two stairs
        a, b = cost[0], cost[1]
        if n == 2:
            return min(a, b)
        for i in range(2, n):
            c = min(a, b) + cost[i]
            a = b
            b = c
        return min(a, b)
