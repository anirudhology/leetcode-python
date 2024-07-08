import unittest
from problems.string.group_anagrams import GroupAnagrams


class GroupAnagramsTest(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(GroupAnagrams.groupAnagrams([]), [])

    def test_null_array(self):
        # noinspection PyTypeChecker
        self.assertEqual(GroupAnagrams.groupAnagrams(None), [])

    def test_single_element_array(self):
        self.assertEqual(GroupAnagrams.groupAnagrams(["a"]), [["a"]])

    def test_multiple_anagrams(self):
        result = GroupAnagrams.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_no_anagrams(self):
        result = GroupAnagrams.groupAnagrams(["abc", "def", "ghi"])
        expected = [["abc"], ["def"], ["ghi"]]
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

if __name__ == '__main__':
    unittest.main()
