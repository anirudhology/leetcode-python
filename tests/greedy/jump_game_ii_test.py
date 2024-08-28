import unittest

from problems.greedy.jump_game_ii import JumpGameII


class TestJumpGameII(unittest.TestCase):

    def test_single_element_array(self):
        jump_game = JumpGameII()
        self.assertEqual(jump_game.jump([0]), 0)

    def test_multiple_jumps_required(self):
        jump_game = JumpGameII()
        self.assertEqual(jump_game.jump([2, 3, 1, 1, 4]), 2)

    def test_maximum_jump_at_each_step(self):
        jump_game = JumpGameII()
        self.assertEqual(jump_game.jump([5, 4, 3, 2, 1, 0]), 1)

    def test_array_with_zeros_not_blocking_path(self):
        jump_game = JumpGameII()
        self.assertEqual(jump_game.jump([2, 0, 2, 0, 1]), 2)


if __name__ == '__main__':
    unittest.main()
