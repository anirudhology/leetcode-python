import unittest
from problems.string.valid_anagram import ValidAnagram


class ValidAnagramTest(unittest.TestCase):

    def setUp(self):
        self.valid_anagram = ValidAnagram()

    def test_anagrams(self):
        self.assertTrue(self.valid_anagram.isAnagram("listen", "silent"))
        self.assertTrue(self.valid_anagram.isAnagram("triangle", "integral"))
        self.assertTrue(self.valid_anagram.isAnagram("anagram", "nagaram"))

    def test_non_anagrams(self):
        self.assertFalse(self.valid_anagram.isAnagram("hello", "world"))
        self.assertFalse(self.valid_anagram.isAnagram("rat", "car"))
        self.assertFalse(self.valid_anagram.isAnagram("abcd", "abce"))

    def test_different_lengths(self):
        self.assertFalse(self.valid_anagram.isAnagram("abc", "abcd"))
        self.assertFalse(self.valid_anagram.isAnagram("a", ""))

    def test_empty_strings(self):
        self.assertTrue(self.valid_anagram.isAnagram("", ""))

    def test_repeated_characters(self):
        self.assertTrue(self.valid_anagram.isAnagram("aabbcc", "abcabc"))
        self.assertFalse(self.valid_anagram.isAnagram("aabbcc", "aabbc"))

    def test_single_characters(self):
        self.assertTrue(self.valid_anagram.isAnagram("a", "a"))
        self.assertFalse(self.valid_anagram.isAnagram("a", "b"))


if __name__ == '__main__':
    unittest.main()
