class PalindromicSubstrings:
    def countSubstrings(self, s: str) -> int:
        # Special case
        if s is None or len(s) == 0:
            return 0
        # Total number of palindromic substrings
        count = 0
        # Process the string by taking each index as the middle
        # and expand both sides from it
        for i in range(len(s)):
            count += self.expand_from_center(s, i, i)
            count += self.expand_from_center(s, i, i + 1)
        return count

    @staticmethod
    def expand_from_center(s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count
