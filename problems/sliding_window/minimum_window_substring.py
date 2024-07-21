class MinimumWindowSubstring:
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        # Array to store the frequencies of characters in string t
        frequencies = [0] * 128
        for c in t:
            frequencies[ord(c)] += 1
        # Left and right pointers for the sliding window
        left, right = 0, 0
        # Length of s
        n = len(s)
        # Count of characters in string t
        count = len(t)
        # Minimum length of the window
        min_length = float('inf')
        # Start index of the window
        start = 0
        # Process the string
        while right < n:
            # If the current character also exists in t
            if frequencies[ord(s[right])] > 0:
                count -= 1
            # Reduce the frequency of this character
            frequencies[ord(s[right])] -= 1
            right += 1
            # If we have found all the characters in t
            while count == 0:
                if right - left < min_length:
                    min_length = right - left
                    start = left
                # Check if the character at left exists in t
                if frequencies[ord(s[left])] == 0:
                    count += 1
                frequencies[ord(s[left])] += 1
                left += 1
        return "" if min_length == float('inf') else s[start:start + min_length]
