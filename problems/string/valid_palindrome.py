class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        # Special case
        if s is None or len(s) == 0:
            return True
        # Left and right pointers
        left, right = 0, len(s) - 1
        # Process the strings from both ends
        while left <= right:
            if not self.isAlphanumeric(s[left]):
                left += 1
                continue
            if not self.isAlphanumeric(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    @staticmethod
    def isAlphanumeric(c: str) -> bool:
        return ((ord('a') <= ord(c) <= ord('z'))
                or ((ord('A') <= ord(c) <= ord('Z'))
                    or (ord('0') <= ord(c) <= ord('9'))))
