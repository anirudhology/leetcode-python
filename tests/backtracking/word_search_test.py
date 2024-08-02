import unittest
from copy import deepcopy

from problems.backtracking.word_search import WordSearch


class TestWordSearch(unittest.TestCase):

    def setUp(self):
        self.word_search = WordSearch()

    def test_word_exists(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertTrue(self.word_search.exist(deepcopy(board), "ABCCED"))
        self.assertTrue(self.word_search.exist(deepcopy(board), "SEE"))

    def test_word_not_exists(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertFalse(self.word_search.exist(deepcopy(board), "ABCB"))
        self.assertFalse(self.word_search.exist(deepcopy(board), "ABCD"))

    def test_single_char_board(self):
        board = [['A']]
        self.assertTrue(self.word_search.exist(deepcopy(board), "A"))
        self.assertFalse(self.word_search.exist(deepcopy(board), "B"))

    def test_empty_board(self):
        board = []
        self.assertFalse(self.word_search.exist(board, "A"))

    def test_empty_word(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertFalse(self.word_search.exist(deepcopy(board), ""))

    def test_null_word(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        # noinspection PyTypeChecker
        self.assertFalse(self.word_search.exist(deepcopy(board), None))

    def test_word_longer_than_board(self):
        board = [
            ['A', 'B', 'C'],
            ['S', 'F', 'E'],
            ['A', 'D', 'E']
        ]
        self.assertFalse(self.word_search.exist(deepcopy(board), "ABCDEE"))

    def test_complex_case(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertTrue(self.word_search.exist(deepcopy(board), "ABCCED"))
        self.assertTrue(self.word_search.exist(deepcopy(board), "SEE"))
        self.assertFalse(self.word_search.exist(deepcopy(board), "ABCB"))

    def test_word_with_dots(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertFalse(self.word_search.exist(deepcopy(board), "A.C.E"))

    def test_word_with_special_chars(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertFalse(self.word_search.exist(deepcopy(board), "AB#C"))


if __name__ == '__main__':
    unittest.main()
