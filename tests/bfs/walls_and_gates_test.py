import unittest

from problems.bfs.walls_and_gates import WallsAndGates


class TestWallsAndGates(unittest.TestCase):

    def setUp(self):
        self.walls_and_gates = WallsAndGates()

    def test_null_rooms(self):
        # noinspection PyTypeChecker
        self.assertIsNone(self.walls_and_gates.islandsAndTreasure(None))

    def test_empty_rooms(self):
        rooms = []
        self.assertEqual(self.walls_and_gates.islandsAndTreasure(rooms), rooms)

    def test_single_room_with_gate(self):
        rooms = [[0]]
        expected = [[0]]
        self.assertEqual(self.walls_and_gates.islandsAndTreasure(rooms), expected)

    def test_single_room_with_wall(self):
        rooms = [[-1]]
        expected = [[-1]]
        self.assertEqual(self.walls_and_gates.islandsAndTreasure(rooms), expected)

    def test_single_room_with_empty(self):
        rooms = [[float('inf')]]
        expected = [[float('inf')]]
        # noinspection PyTypeChecker
        self.assertEqual(self.walls_and_gates.islandsAndTreasure(rooms), expected)

    def test_grid_with_multiple_gates(self):
        rooms = [
            [float('inf'), -1, 0, float('inf')],
            [float('inf'), float('inf'), float('inf'), -1],
            [float('inf'), -1, float('inf'), -1],
            [0, -1, float('inf'), float('inf')]
        ]
        expected = [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4]
        ]
        self.assertEqual(self.walls_and_gates.islandsAndTreasure(rooms), expected)

    def test_grid_with_no_gates(self):
        rooms = [
            [float('inf'), -1, float('inf'), float('inf')],
            [float('inf'), float('inf'), float('inf'), -1],
            [float('inf'), -1, float('inf'), -1],
            [float('inf'), -1, float('inf'), float('inf')]
        ]
        expected = rooms
        self.assertEqual(self.walls_and_gates.islandsAndTreasure(rooms), expected)


if __name__ == '__main__':
    unittest.main()
