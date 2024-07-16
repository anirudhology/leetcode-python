import unittest

from problems.stack.daily_temperatures import DailyTemperatures


class DailyTemperaturesTest(unittest.TestCase):
    def test_none_input(self):
        # noinspection PyTypeChecker
        self.assertIsNone(DailyTemperatures.dailyTemperatures(None))

    def test_empty_input(self):
        self.assertEqual(DailyTemperatures.dailyTemperatures([]), [])

    def test_single_element(self):
        self.assertEqual(DailyTemperatures.dailyTemperatures([30]), [0])

    def test_increasing_temperatures(self):
        self.assertEqual(DailyTemperatures.dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0])

    def test_decreasing_temperatures(self):
        self.assertEqual(DailyTemperatures.dailyTemperatures([60, 50, 40, 30]), [0, 0, 0, 0])

    def test_mixed_temperatures(self):
        self.assertEqual(DailyTemperatures.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
                         [1, 1, 4, 2, 1, 1, 0, 0])

    def test_all_same_temperatures(self):
        self.assertEqual(DailyTemperatures.dailyTemperatures([50, 50, 50, 50]), [0, 0, 0, 0])

    def test_random_order_temperatures(self):
        self.assertEqual(DailyTemperatures.dailyTemperatures([30, 31, 32, 33]), [1, 1, 1, 0])


if __name__ == "__main__":
    unittest.main()
