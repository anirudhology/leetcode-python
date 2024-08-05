import unittest

from problems.backtracking.letter_combinations_of_a_phone_number import LetterCombinationsOfAPhoneNumber


class LetterCombinationsOfAPhoneNumberLetter(unittest.TestCase):

    def setUp(self):
        self.letter_combinations_of_a_phone_number = LetterCombinationsOfAPhoneNumber()

    def test_letter_combinations(self):
        self.assertEqual(self.letter_combinations_of_a_phone_number.letterCombinations("23"),
                         ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(self.letter_combinations_of_a_phone_number.letterCombinations(""), [])
        self.assertEqual(self.letter_combinations_of_a_phone_number.letterCombinations("2"), ["a", "b", "c"])
        self.assertEqual(self.letter_combinations_of_a_phone_number.letterCombinations("9"), ["w", "x", "y", "z"])
        self.assertEqual(self.letter_combinations_of_a_phone_number.letterCombinations("1"), [])
        self.assertEqual(self.letter_combinations_of_a_phone_number.letterCombinations("10"), [])


if __name__ == '__main__':
    unittest.main()
