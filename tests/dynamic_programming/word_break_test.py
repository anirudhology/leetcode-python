import unittest

from problems.dynamic_programming.word_break import WordBreak


class TestWordBreak(unittest.TestCase):

    def setUp(self):
        self.word_break = WordBreak()

    def test_word_break(self):
        # Test case for null input string
        # noinspection PyTypeChecker
        self.assertFalse(self.word_break.wordBreak(None, ["leet", "code"]))

        # Test case for empty string
        self.assertFalse(self.word_break.wordBreak("", ["leet", "code"]))

        # Test case for null wordDict
        # noinspection PyTypeChecker
        self.assertFalse(self.word_break.wordBreak("leetcode", None))

        # Test case for empty wordDict
        self.assertFalse(self.word_break.wordBreak("leetcode", []))

        # Test case for string that can be segmented
        self.assertTrue(self.word_break.wordBreak("leetcode", ["leet", "code"]))

        # Test case for string that cannot be segmented
        self.assertFalse(self.word_break.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

        # Test case for string with overlapping words
        self.assertTrue(self.word_break.wordBreak("applepenapple", ["apple", "pen"]))

        # Test case for string with single character words
        self.assertTrue(self.word_break.wordBreak("abcd", ["a", "b", "c", "d"]))


if __name__ == '__main__':
    unittest.main()
