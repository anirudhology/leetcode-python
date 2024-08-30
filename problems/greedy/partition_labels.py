from typing import List


class PartitionLabels:
    @staticmethod
    def partitionLabels(s: str) -> List[int]:
        # List to store the sizes of partitions
        sizes = []
        # Special case
        if not s:
            return sizes

        # Array to store last positions of characters
        last_position = [0] * 26
        for i in range(len(s)):
            last_position[ord(s[i]) - ord('a')] = i

        # Pointers for the window
        left, right = 0, 0
        # Traverse through the string again
        for i in range(len(s)):
            right = max(right, last_position[ord(s[i]) - ord('a')])
            if right == i:
                sizes.append(right - left + 1)
                left = i + 1

        return sizes
