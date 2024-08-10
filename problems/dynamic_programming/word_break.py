from typing import List


class WordBreak:
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        # Special case
        if s is None or len(s) == 0 or wordDict is None or len(wordDict) == 0:
            return False
        n = len(s)
        # Add words to the set for O(1) search
        words = set(wordDict)
        # Lookup table to store if substring until the current index
        # is present in the dictionary or not
        lookup = [False] * (n + 1)
        # Empty string is always present
        lookup[0] = True
        # Process the array
        for i in range(1, n + 1):
            for j in range(i):
                if lookup[j] and s[j:i] in words:
                    lookup[i] = True
                    break
        return lookup[n]
