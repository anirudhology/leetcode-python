import unittest

from problems.dynamic_programming.interleaving_string import InterleavingString


class TestInterleavingString(unittest.TestCase):

    def setUp(self):
        self.interleaving_string = InterleavingString()

    def test_interleave(self):
        self.assertTrue(self.interleaving_string.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
        self.assertFalse(self.interleaving_string.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
        self.assertTrue(self.interleaving_string.isInterleave("", "", ""))
        self.assertTrue(self.interleaving_string.isInterleave("a", "", "a"))
        self.assertTrue(self.interleaving_string.isInterleave("", "b", "b"))
        self.assertFalse(self.interleaving_string.isInterleave("abc", "def", "abdccfe"))

    def test_edge_cases(self):
        self.assertFalse(self.interleaving_string.isInterleave("abc", "def", "abcdefg"))
        self.assertTrue(self.interleaving_string.isInterleave("abc", "def", "adbcef"))
        self.assertFalse(self.interleaving_string.isInterleave("", "a", "b"))


if __name__ == '__main__':
    unittest.main()
