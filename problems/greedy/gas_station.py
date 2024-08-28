from typing import List


class GasStation:
    @staticmethod
    def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
        # Local effective fuel - fuel if we start from current index
        local_fuel = 0
        # Global effective fuel - fuel left after the journey
        global_fuel = 0
        # Index to start the journey from
        index = 0
        # Process the arrays
        for i in range(len(gas)):
            local_fuel += gas[i] - cost[i]
            global_fuel += gas[i] - cost[i]
            # Check if the fuel becomes negative
            if local_fuel < 0:
                local_fuel = 0
                index = i + 1
        return index if global_fuel >= 0 else -1
