class TimeMap:

    def __init__(self):
        self.entries = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.entries:
            self.entries[key] = Node()
        node = self.entries[key]
        node.values.append(value)
        node.timestamps.append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.entries:
            return ""
        # Get values and timestamps
        values = self.entries[key].values
        timestamps = self.entries[key].timestamps
        # Left and right pointers for binary search
        left, right = 0, len(timestamps) - 1
        # Final result
        result = ""
        while left <= right:
            middle = left + (right - left) // 2
            if timestamps[middle] <= timestamp:
                result = values[middle]
                left = middle + 1
            else:
                right = middle - 1
        return result


class Node:

    def __init__(self):
        self.values = list()
        self.timestamps = list()
