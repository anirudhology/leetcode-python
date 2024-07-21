import unittest

from problems.sliding_window.permutation_in_string import PermutationInString


class PermutationInStringTest(unittest.TestCase):

    def test_empty_s1(self):
        self.assertTrue(PermutationInString.checkInclusion("", "anything"))

    def test_empty_s2(self):
        self.assertFalse(PermutationInString.checkInclusion("anything", ""))

    def test_s1_longer_than_s2(self):
        self.assertFalse(PermutationInString.checkInclusion("longstring", "short"))

    def test_exact_match(self):
        self.assertTrue(PermutationInString.checkInclusion("abc", "cba"))

    def test_permutation_in_middle(self):
        self.assertTrue(PermutationInString.checkInclusion("ab", "eidbaooo"))

    def test_permutation_at_start(self):
        self.assertTrue(PermutationInString.checkInclusion("ab", "abdcba"))

    def test_permutation_at_end(self):
        self.assertTrue(PermutationInString.checkInclusion("ab", "eidboaooab"))

    def test_no_permutation(self):
        self.assertFalse(PermutationInString.checkInclusion("ab", "eidboaoo"))

    def test_repeated_characters_in_s1(self):
        self.assertTrue(PermutationInString.checkInclusion("aabb", "bbbaaabbcc"))

    def test_different_characters(self):
        self.assertFalse(PermutationInString.checkInclusion("abc", "defghijkl"))


if __name__ == '__main__':
    unittest.main()
