import unittest

from problems.stack.min_stack import MinStack


class MinStackTeEst(unittest.TestCase):

    def setUp(self):
        self.min_stack = MinStack()

    def test_push_and_top(self):
        self.min_stack.push(1)
        self.assertEqual(self.min_stack.top(), 1)

        self.min_stack.push(2)
        self.assertEqual(self.min_stack.top(), 2)

        self.min_stack.push(-1)
        self.assertEqual(self.min_stack.top(), -1)

    def test_pop(self):
        self.min_stack.push(1)
        self.min_stack.push(2)
        self.min_stack.push(3)

        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 2)

        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 1)

    def test_get_min(self):
        self.min_stack.push(1)
        self.assertEqual(self.min_stack.getMin(), 1)

        self.min_stack.push(2)
        self.assertEqual(self.min_stack.getMin(), 1)

        self.min_stack.push(-1)
        self.assertEqual(self.min_stack.getMin(), -1)

        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 1)

    def test_mixed_operations(self):
        self.min_stack.push(3)
        self.min_stack.push(5)
        self.assertEqual(self.min_stack.getMin(), 3)

        self.min_stack.push(2)
        self.min_stack.push(1)
        self.assertEqual(self.min_stack.getMin(), 1)

        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 2)

        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 3)

        self.assertEqual(self.min_stack.top(), 5)


if __name__ == '__main__':
    unittest.main()
