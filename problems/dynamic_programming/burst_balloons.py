from typing import List


class BurstBalloons:
    @staticmethod
    def maxCoins(nums: List[int]) -> int:
        # Array of balloons with two dummy balloons
        balloons = [1] * (len(nums) + 2)
        n = len(balloons)
        for i in range(1, len(nums) + 1):
            balloons[i] = nums[i - 1]
        # Lookup table
        lookup = [[-1] * (n - 1) for _ in range(n - 1)]

        def burst(balloons: List[int], i: int, j: int, lookup: List[List[int]]):
            # Base case
            if i > j:
                return 0
            # If there is only one balloon
            if i == j:
                temp = balloons[i]
                if i - 1 >= 0:
                    temp *= balloons[i - 1]
                if j + 1 < len(balloons):
                    temp *= balloons[j + 1]
                return temp

            # If we have already calculated the result
            if lookup[i][j] != -1:
                return lookup[i][j]

            # Score
            score = 0
            # We burst each balloon in the last in the range i to j
            for k in range(i, j + 1):
                # Burst the k-th balloon in the last after bursting balloons
                # in the range (i, k - 1) and (k + 1, j)
                temp = balloons[k]
                if i - 1 >= 0:
                    temp *= balloons[i - 1]
                if j + 1 < len(balloons):
                    temp *= balloons[j + 1]

                # Recursively burst left and right halves
                temp += (burst(balloons, i, k - 1, lookup) + burst(balloons, k + 1, j, lookup))
                # Update score, if required
                score = max(score, temp)

            lookup[i][j] = score
            return score

        # Burst all balloons in the range 1, n - 2
        return burst(balloons, 1, n - 2, lookup)
