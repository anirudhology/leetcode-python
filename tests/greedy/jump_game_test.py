import unittest

from problems.greedy.jump_game import JumpGame


class TestJumpGame(unittest.TestCase):

    def test_single_element_array(self):
        jump_game = JumpGame()
        self.assertTrue(jump_game.canJump([0]))

    def test_all_zeros_except_first(self):
        jump_game = JumpGame()
        self.assertFalse(jump_game.canJump([1, 0, 0, 0]))

    def test_sufficient_jumps(self):
        jump_game = JumpGame()
        self.assertTrue(jump_game.canJump([2, 3, 1, 1, 4]))

    def test_insufficient_jumps(self):
        jump_game = JumpGame()
        self.assertFalse(jump_game.canJump([3, 2, 1, 0, 4]))


if __name__ == '__main__':
    unittest.main()
