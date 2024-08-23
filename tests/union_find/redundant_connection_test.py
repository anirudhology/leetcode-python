import unittest

from problems.union_find.redundant_connection import RedundantConnection


class TestRedundantConnection(unittest.TestCase):
    def test_findRedundantConnection(self):
        redundant_connection = RedundantConnection()
        self.assertEqual(redundant_connection.findRedundantConnection([[1, 2], [1, 3], [2, 3]]), [2, 3])
        self.assertEqual(redundant_connection.findRedundantConnection([[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]), [1, 5])


if __name__ == "__main__":
    unittest.main()
