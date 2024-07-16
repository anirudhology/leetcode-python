import unittest

from problems.stack.car_fleet import CarFleet


class CarFleetTest(unittest.TestCase):

    def setUp(self):
        self.cf = CarFleet()

    def test_no_cars(self):
        self.assertEqual(self.cf.carFleet(10, [], []), 0)

    def test_negative_target(self):
        self.assertEqual(self.cf.carFleet(-10, [0, 3, 5], [1, 2, 1]), 0)

    def test_single_car(self):
        self.assertEqual(self.cf.carFleet(10, [5], [2]), 1)

    def test_all_cars_same_position_and_speed(self):
        self.assertEqual(self.cf.carFleet(10, [1, 1, 1], [1, 1, 1]), 1)

    def test_all_cars_different_position_and_speed(self):
        self.assertEqual(self.cf.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)

    def test_cars_with_same_position_different_speed(self):
        self.assertEqual(self.cf.carFleet(10, [3, 3, 3], [1, 2, 3]), 1)

    def test_cars_with_same_speed_different_position(self):
        self.assertEqual(self.cf.carFleet(10, [0, 4, 2], [2, 2, 2]), 3)

    def test_cars_forming_one_fleet(self):
        self.assertEqual(self.cf.carFleet(10, [6, 8], [3, 2]), 2)

    def test_cars_forming_multiple_fleets(self):
        self.assertEqual(self.cf.carFleet(15, [5, 10, 0, 7], [2, 1, 3, 2]), 1)

    def test_example_case(self):
        self.assertEqual(self.cf.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)


if __name__ == '__main__':
    unittest.main()
