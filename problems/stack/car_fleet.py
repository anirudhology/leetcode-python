from typing import List


class CarFleet:
    @staticmethod
    def carFleet(target: int, position: List[int], speed: List[int]) -> int:
        # Special case
        if target < 0 or position is None or len(position) == 0 or speed is None or len(speed) == 0:
            return 0
        # Length of the array
        n = len(position)
        # Array to store the position along with their required time to reach target
        cars = [[0 for _ in range(2)] for _ in range(n)]
        for i in range(n):
            cars[i][0] = position[i]
            # noinspection PyTypeChecker
            cars[i][1] = (target - position[i]) / speed[i]
        # Sort the array in descending array by position
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        # Last time registered
        last_time = 0
        # Fleet counter
        fleets = 0
        # Process the cars array
        for i in range(n):
            if cars[i][1] > last_time:
                fleets += 1
                last_time = cars[i][1]
        return fleets