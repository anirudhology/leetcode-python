class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str | None:
        # Special case
        if s is None or len(s) == 0:
            return s
        # Start and end pointers for longest palindromic substring
        start, end = 0, 0
        # Process the string
        for i in range(len(s)):
            # Expand for odd and even lengths
            odd_length = self.expand_from_center(s, i, i)
            even_length = self.expand_from_center(s, i, i + 1)
            # Max length of two
            max_length = max(odd_length, even_length)
            if max_length > end - start:
                start = i - (max_length - 1) // 2
                end = i + max_length // 2
        return s[start:end + 1]

    @staticmethod
    def expand_from_center(s: str, left: int, right: int):
        if left > right:
            return 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
