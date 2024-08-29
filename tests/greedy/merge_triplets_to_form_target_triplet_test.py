import unittest

from problems.greedy.merge_triplets_to_form_target_triplet import MergeTripletsToFormTargetTriplet


class TestMergeTripletsToFormTargetTriplet(unittest.TestCase):

    def setUp(self):
        self.merge_triplets = MergeTripletsToFormTargetTriplet()

    def test_merge_triplets_all_present(self):
        self.assertTrue(self.merge_triplets.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))

    def test_merge_triplets_not_all_present(self):
        self.assertFalse(self.merge_triplets.mergeTriplets([[2, 3, 4], [1, 2, 3], [1, 2, 3]], [3, 2, 5]))

    def test_merge_triplets_single_triplet_match(self):
        self.assertTrue(self.merge_triplets.mergeTriplets([[2, 5, 3]], [2, 5, 3]))

    def test_merge_triplets_empty_triplets(self):
        self.assertFalse(self.merge_triplets.mergeTriplets([], [1, 2, 3]))

    def test_merge_triplets_large_values(self):
        self.assertTrue(self.merge_triplets.mergeTriplets([[100000, 100000, 100000], [99999, 99999, 99999]],
                                                          [100000, 100000, 100000]))

    def test_merge_triplets_zero_target(self):
        self.assertTrue(self.merge_triplets.mergeTriplets([[0, 0, 0], [1, 1, 1], [0, 1, 0]], [0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
