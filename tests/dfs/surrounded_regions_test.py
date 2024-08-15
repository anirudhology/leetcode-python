import unittest

from problems.dfs.surrounded_regions import SurroundedRegions


class TestSurroundedRegions(unittest.TestCase):

    def test_solve_empty_board(self):
        solver = SurroundedRegions()
        board = []
        self.assertEqual(solver.solve(board), board)

    def test_solve_null_board(self):
        solver = SurroundedRegions()
        board = None
        # noinspection PyTypeChecker
        self.assertEqual(solver.solve(board), board)

    def test_solve_single_cell_o(self):
        solver = SurroundedRegions()
        board = [['O']]
        expected = [['O']]
        self.assertEqual(solver.solve(board), expected)

    def test_solve_single_cell_x(self):
        solver = SurroundedRegions()
        board = [['X']]
        expected = [['X']]
        self.assertEqual(solver.solve(board), expected)

    def test_solve_small_board(self):
        solver = SurroundedRegions()
        board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        expected = [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        self.assertEqual(solver.solve(board), expected)


if __name__ == '__main__':
    unittest.main()
