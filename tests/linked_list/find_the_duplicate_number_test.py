import unittest

from problems.linked_list.find_the_duplicate_number import FindTheDuplicateNumber


class FindTheDuplicateNumberTest(unittest.TestCase):

    def setUp(self):
        self.finder = FindTheDuplicateNumber()

    def test_find_duplicate_single_duplicate(self):
        self.assertEqual(self.finder.findDuplicate([1, 3, 4, 2, 2]), 2)

    def test_find_duplicate_multiple_duplicates(self):
        self.assertEqual(self.finder.findDuplicate([3, 1, 3, 4, 2]), 3)

    def test_find_duplicate_at_start(self):
        self.assertEqual(self.finder.findDuplicate([1, 1]), 1)

    def test_find_duplicate_large_input(self):
        self.assertEqual(self.finder.findDuplicate([1, 3, 4, 2, 2]), 2)

    def test_find_duplicate_single_number(self):
        self.assertEqual(self.finder.findDuplicate([1, 1]), 1)

    def test_find_duplicate_random_order(self):
        self.assertEqual(self.finder.findDuplicate([4, 2, 1, 3, 2]), 2)


if __name__ == '__main__':
    unittest.main()
