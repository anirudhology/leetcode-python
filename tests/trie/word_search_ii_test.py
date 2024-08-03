import unittest

from problems.trie.word_search_ii import WordSearchII


class WordSearchIITest(unittest.TestCase):
    def setUp(self):
        self.word_search_ii = WordSearchII()

    def test_find_words_basic(self):
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ]
        words = ["oath", "pea", "eat", "rain"]
        expected_result = ["eat", "oath"]
        self.assertCountEqual(self.word_search_ii.findWords(board, words), expected_result)

    def test_find_words_no_match(self):
        board = [
            ['a', 'b'],
            ['c', 'd']
        ]
        words = ["xyz", "uvw"]
        expected_result = []
        self.assertCountEqual(self.word_search_ii.findWords(board, words), expected_result)

    def test_find_words_empty_board(self):
        board = []
        words = ["word"]
        expected_result = []
        self.assertCountEqual(self.word_search_ii.findWords(board, words), expected_result)

    def test_find_words_empty_words(self):
        board = [
            ['a', 'b'],
            ['c', 'd']
        ]
        words = []
        expected_result = []
        self.assertCountEqual(self.word_search_ii.findWords(board, words), expected_result)

    def test_find_words_empty_board_and_words(self):
        board = []
        words = []
        expected_result = []
        self.assertCountEqual(self.word_search_ii.findWords(board, words), expected_result)

    def test_find_words_no_matching_words(self):
        board = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        words = ["xyz", "jkl"]
        expected_result = []
        self.assertCountEqual(self.word_search_ii.findWords(board, words), expected_result)

    def test_find_words_with_duplicates(self):
        board = [
            ['a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a']
        ]
        words = ["aaaa", "aaa", "aa"]
        expected_result = ["aa", "aaa", "aaaa"]
        self.assertCountEqual(self.word_search_ii.findWords(board, words), expected_result)

    def test_find_words_with_single_cell_board(self):
        board = [['a']]
        words = ["a", "b"]
        expected_result = ["a"]
        self.assertCountEqual(self.word_search_ii.findWords(board, words), expected_result)


if __name__ == '__main__':
    unittest.main()
