import unittest

from problems.heap.task_scheduler import TaskScheduler


class TestTaskScheduler(unittest.TestCase):

    def test_empty_tasks(self):
        task_scheduler = TaskScheduler()
        self.assertEqual(task_scheduler.leastInterval([], 2), 0)

    def test_null_tasks(self):
        task_scheduler = TaskScheduler()
        # noinspection PyTypeChecker
        self.assertEqual(task_scheduler.leastInterval(None, 2), 0)

    def test_single_task(self):
        task_scheduler = TaskScheduler()
        self.assertEqual(task_scheduler.leastInterval(['A'], 2), 1)

    def test_multiple_tasks_with_cooldown(self):
        task_scheduler = TaskScheduler()
        self.assertEqual(task_scheduler.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2), 8)

    def test_multiple_tasks_no_cooldown(self):
        task_scheduler = TaskScheduler()
        self.assertEqual(task_scheduler.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 0), 6)

    def test_complex_task_pattern(self):
        task_scheduler = TaskScheduler()
        self.assertEqual(task_scheduler.leastInterval(['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'], 2), 9)


if __name__ == '__main__':
    unittest.main()
