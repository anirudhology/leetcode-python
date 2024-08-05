from typing import List


class PalindromePartitioning:
    def partition(self, s: str) -> List[List[str]]:
        # List to store the final partitions
        partitions = []
        # Special case
        if s is None or len(s) == 0:
            return partitions
        # Perform backtracking
        self.backtrack(s, 0, [], partitions)
        return partitions

    def backtrack(self, s: str, index: int, current: List[str], partitions: List[List[str]]):
        # Base case
        if index == len(s):
            partitions.append(list(current))
            return
        for i in range(index, len(s)):
            # Check if the current substring is palindrome
            if self.is_palindrome(s, index, i):
                current.append(s[index:i + 1])
                self.backtrack(s, i + 1, current, partitions)
                current.pop()

    @staticmethod
    def is_palindrome(s: str, left: int, right: int):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
