import unittest

from problems.greedy.hand_of_straights import HandOfStraights


class TestHandOfStraights(unittest.TestCase):

    def test_is_n_straight_hand_valid(self):
        straights = HandOfStraights()
        hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
        group_size = 3
        self.assertTrue(straights.isNStraightHand(hand, group_size))

    def test_is_n_straight_hand_invalid(self):
        straights = HandOfStraights()
        hand = [1, 2, 3, 4, 5]
        group_size = 4
        self.assertFalse(straights.isNStraightHand(hand, group_size))

    def test_is_n_straight_hand_empty_hand(self):
        straights = HandOfStraights()
        hand = []
        group_size = 1
        self.assertTrue(straights.isNStraightHand(hand, group_size))  # An empty hand should return true

    def test_is_n_straight_hand_single_group(self):
        straights = HandOfStraights()
        hand = [1, 2, 3]
        group_size = 3
        self.assertTrue(straights.isNStraightHand(hand, group_size))

    def test_is_n_straight_hand_group_size_one(self):
        straights = HandOfStraights()
        hand = [1, 2, 3, 4]
        group_size = 1
        self.assertTrue(straights.isNStraightHand(hand, group_size))  # Every single card is its own group

    def test_is_n_straight_hand_group_size_larger_than_hand(self):
        straights = HandOfStraights()
        hand = [1, 2, 3]
        group_size = 4
        self.assertFalse(straights.isNStraightHand(hand, group_size))  # Group size cannot be larger than the hand size

    def test_is_n_straight_hand_duplicate_cards(self):
        straights = HandOfStraights()
        hand = [1, 1, 2, 2, 3, 3]
        group_size = 3
        self.assertTrue(straights.isNStraightHand(hand, group_size))  # Duplicate cards should still form groups


if __name__ == '__main__':
    unittest.main()
