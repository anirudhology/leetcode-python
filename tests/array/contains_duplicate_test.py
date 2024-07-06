import unittest

from problems.array.contains_duplicate import ContainsDuplicate


class ContainsDuplicateTest(unittest.TestCase):
    def setUp(self):
        self.contains_duplicate = ContainsDuplicate()

    def test_null_array(self):
        nums = None
        self.assertFalse(self.contains_duplicate.containsDuplicate(nums), "Null array should return False")

    def test_empty_array(self):
        nums = []
        self.assertFalse(self.contains_duplicate.containsDuplicate(nums), "Empty array should return False")

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        self.assertFalse(self.contains_duplicate.containsDuplicate(nums), "Array with no duplicates should return False")

    def test_with_duplicates(self):
        nums = [1, 2, 3, 4, 1]
        self.assertTrue(self.contains_duplicate.containsDuplicate(nums), "Array with duplicates should return True")

    def test_single_element(self):
        nums = [1]
        self.assertFalse(self.contains_duplicate.containsDuplicate(nums), "Array with a single element should return False")

    def test_multiple_duplicates(self):
        nums = [1, 1, 1, 1, 1]
        self.assertTrue(self.contains_duplicate.containsDuplicate(nums),
                        "Array with all elements being the same should return True")


if __name__ == '__main__':
    unittest.main()