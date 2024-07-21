class PermutationInString:
    @staticmethod
    def checkInclusion(s1: str, s2: str) -> bool:
        # Special case
        if len(s1) > len(s2):
            return False
        # Array to store the frequencies of characters in s1
        frequencies = [0] * 26
        for c in s1:
            frequencies[ord(c) - ord('a')] += 1
        # Left and right pointers for the sliding window
        left, right = 0, 0
        # Process the string s2
        while right < len(s2):
            frequencies[ord(s2[right]) - ord('a')] -= 1
            while left < len(s2) and frequencies[ord(s2[right]) - ord('a')] < 0:
                frequencies[ord(s2[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(s1):
                return True
            right += 1
        return False
