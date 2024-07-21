class LongestRepeatingCharacterReplacement:
    @staticmethod
    def characterReplacement(s: str, k: int) -> int:
        # Special case
        if s is None or len(s) == 0 or k < 0:
            return 0
        # Left and right pointers for the sliding window
        left, right = 0, 0
        # Array to store the frequencies of characters in the string
        frequencies = [0] * 26
        # Count for most popular character so far
        max_count = 0
        # Longest length
        longest_length = 0
        # Process the strings using sliding window
        while right < len(s):
            # Calculate the frequency of current character
            frequencies[ord(s[right]) - ord('A')] += 1
            frequency = frequencies[ord(s[right]) - ord('A')]
            # Update max_count if required
            max_count = max(max_count, frequency)
            # If there are more than k characters that are not the same as
            # the most popular character, we shift the window
            while right - left + 1 - max_count > k:
                frequencies[ord(s[left]) - ord('A')] -= 1
                left += 1
            longest_length = max(longest_length, right - left + 1)
            right += 1
        return longest_length
