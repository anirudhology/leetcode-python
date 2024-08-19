import unittest

from problems.graph.course_schedule import CourseSchedule


class TestCourseSchedule(unittest.TestCase):

    def setUp(self):
        self.course_schedule = CourseSchedule()

    def test_can_finish_no_prerequisites(self):
        self.assertTrue(self.course_schedule.canFinish(3, []))

    def test_can_finish_valid_prerequisites(self):
        self.assertTrue(self.course_schedule.canFinish(2, [[1, 0]]))

    def test_can_finish_with_cycle(self):
        self.assertFalse(self.course_schedule.canFinish(2, [[1, 0], [0, 1]]))

    def test_can_finish_complex_graph(self):
        self.assertTrue(self.course_schedule.canFinish(4, [[1, 0], [2, 1], [3, 2]]))

    def test_can_finish_isolated_courses(self):
        self.assertTrue(self.course_schedule.canFinish(5, [[1, 0], [3, 2]]))


if __name__ == "__main__":
    unittest.main()
