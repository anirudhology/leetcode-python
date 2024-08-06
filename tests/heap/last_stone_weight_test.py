import unittest

from problems.heap.last_stone_weight import LastStoneWeight


class LastStoneWeightTest(unittest.TestCase):
    def test_last_stone_weight(self):
        last_stone_weight = LastStoneWeight()

        self.assertEqual(last_stone_weight.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)
        self.assertEqual(last_stone_weight.lastStoneWeight([2, 2]), 0)
        self.assertEqual(last_stone_weight.lastStoneWeight([1]), 1)
        self.assertEqual(last_stone_weight.lastStoneWeight([]), 0)
        # noinspection PyTypeChecker
        self.assertEqual(last_stone_weight.lastStoneWeight(None), 0)


if __name__ == '__main__':
    unittest.main()
