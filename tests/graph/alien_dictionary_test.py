import unittest

from problems.graph.alien_dictionary import AlienDictionary


class TestAlienDictionary(unittest.TestCase):

    def setUp(self):
        self.alien_dictionary = AlienDictionary()

    def test_valid_order(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        self.assertEqual(self.alien_dictionary.foreignDictionary(words), "wertf")

    def test_invalid_order_due_to_cycle(self):
        words = ["z", "x", "z"]
        self.assertEqual(self.alien_dictionary.foreignDictionary(words), "")

    def test_invalid_order_due_to_prefix(self):
        words = ["abc", "ab"]
        self.assertEqual(self.alien_dictionary.foreignDictionary(words), "")

    def test_single_word(self):
        words = ["abc"]
        self.assertEqual(self.alien_dictionary.foreignDictionary(words), "abc")

    def test_empty_words(self):
        words = []
        self.assertEqual(self.alien_dictionary.foreignDictionary(words), "")

    def test_no_valid_order(self):
        words = ["a", "b", "c"]
        self.assertEqual(self.alien_dictionary.foreignDictionary(words), "abc")


if __name__ == '__main__':
    unittest.main()
