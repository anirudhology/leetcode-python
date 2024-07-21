class LongestSubstringWithoutRepeatingCharacters:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        # Special case
        if s is None or len(s) == 0:
            return 0
        # Length of the string
        n = len(s)
        # Slow and fast pointers for sliding window
        slow, fast = 0, 0
        # Set to store unique characters
        uniques = set()
        # Longest length
        longest_length = 0
        # Process the string
        while fast < n:
            while fast < n and s[fast] not in uniques:
                uniques.add(s[fast])
                fast += 1
            longest_length = max(longest_length, len(uniques))
            # Remove left most character from the window
            uniques.remove(s[slow])
            slow += 1
        return longest_length
