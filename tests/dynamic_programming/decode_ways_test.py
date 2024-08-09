import unittest

from problems.dynamic_programming.decode_ways import DecodeWays


class DecodeWaysTest(unittest.TestCase):

    def setUp(self):
        self.decode_ways = DecodeWays()

    def test_num_decodings(self):
        # Test case for null string
        # noinspection PyTypeChecker
        self.assertEqual(self.decode_ways.numDecodings(None), 0)

        # Test case for empty string
        self.assertEqual(self.decode_ways.numDecodings(""), 0)

        # Test case for string with a single character
        self.assertEqual(self.decode_ways.numDecodings("1"), 1)

        # Test case for string with multiple characters
        self.assertEqual(self.decode_ways.numDecodings("12"), 2)  # "AB" (1 2) or "L" (12)

        # Test case for string with leading zeros
        self.assertEqual(self.decode_ways.numDecodings("012"), 0)

        # Test case for string with multiple decoding possibilities
        self.assertEqual(self.decode_ways.numDecodings("226"), 3)  # "BBF" (2 2 6), "BZ" (2 26), "VF" (22 6)

        # Test case for string with no valid decodings
        self.assertEqual(self.decode_ways.numDecodings("30"), 0)

        # Test case for string with multiple valid decodings
        self.assertEqual(self.decode_ways.numDecodings("11106"), 2)


if __name__ == '__main__':
    unittest.main()
