import unittest

from problems.backtracking.n_queens import NQueens


class NQueensTest(unittest.TestCase):

    def setUp(self):
        self.nqueens = NQueens()

    def test_solve_n_queens(self):
        self.assertEqual(self.nqueens.solveNQueens(4), [
            ['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']
        ])
        self.assertEqual(self.nqueens.solveNQueens(1), [["Q"]])
        self.assertEqual(self.nqueens.solveNQueens(0), [])
        self.assertEqual(self.nqueens.solveNQueens(2), [])
        self.assertEqual(self.nqueens.solveNQueens(3), [])


if __name__ == '__main__':
    unittest.main()
