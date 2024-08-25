import unittest

from problems.bfs.word_ladder import WordLadder


class TestWordLadder(unittest.TestCase):

    def test_ladder_length_word_exists(self):
        word_ladder = WordLadder()
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        result = word_ladder.ladderLength("hit", "cog", word_list)
        self.assertEqual(result, 5)

    def test_ladder_length_word_does_not_exist(self):
        word_ladder = WordLadder()
        word_list = ["hot", "dot", "dog", "lot", "log"]
        result = word_ladder.ladderLength("hit", "cog", word_list)
        self.assertEqual(result, 0)

    def test_ladder_length_begin_word_equals_end_word(self):
        word_ladder = WordLadder()
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        result = word_ladder.ladderLength("hit", "hit", word_list)
        self.assertEqual(result, 0)

    def test_ladder_length_empty_word_list(self):
        word_ladder = WordLadder()
        word_list = []
        result = word_ladder.ladderLength("hit", "cog", word_list)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
