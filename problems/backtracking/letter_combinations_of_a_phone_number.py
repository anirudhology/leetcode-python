from typing import List


class LetterCombinationsOfAPhoneNumber:
    def letterCombinations(self, digits: str) -> List[str]:
        # List to store the combinations
        combinations = []
        # Special case
        if digits is None or len(digits) == 0:
            return combinations

        # Mappings for digits
        mappings = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        # Peform backtracking
        self.backtrack(digits, 0, "", mappings, combinations)
        return combinations

    def backtrack(self, digits: str, index: int, combination: str, mappings: List[str], combinations: List[str]):
        # Base case
        if index == len(digits):
            combinations.append(combination)
            return
        # Get current letters
        letters = mappings[ord(digits[index]) - ord('0')]
        for letter in letters:
            self.backtrack(digits, index + 1, combination + letter, mappings, combinations)
