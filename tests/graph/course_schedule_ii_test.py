import unittest

from problems.graph.course_schedule_ii import CourseScheduleII


class TestCourseScheduleII(unittest.TestCase):

    def setUp(self):
        self.course_schedule = CourseScheduleII()

    def test_find_order_no_prerequisites(self):
        self.assertEqual(self.course_schedule.findOrder(3, []), [0, 1, 2])

    def test_find_order_valid_prerequisites(self):
        self.assertEqual(self.course_schedule.findOrder(2, [[1, 0]]), [0, 1])

    def test_find_order_with_cycle(self):
        self.assertEqual(self.course_schedule.findOrder(2, [[1, 0], [0, 1]]), [])

    def test_find_order_complex_graph(self):
        self.assertEqual(self.course_schedule.findOrder(4, [[1, 0], [2, 1], [3, 2]]), [0, 1, 2, 3])

    def test_find_order_isolated_courses(self):
        self.assertEqual(self.course_schedule.findOrder(5, [[1, 0], [3, 2]]), [0, 2, 4, 1, 3])


if __name__ == '__main__':
    unittest.main()
