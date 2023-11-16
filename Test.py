import unittest
import pygame

class GuessingGameTest(unittest.TestCase):

    def setUp(self):
        self.game = GuessingGameTest()

#This unit test checks that the function generates a list of 18 options and 36 spaces.
    def test_generate_board(self):
        game = GuessingGameTest()
        self.assertEqual(len(self.game.options_list), 18)
        self.assertEqual(len(self.game.spaces), 36)

#It checks that the function correctly draws a restart button at the top left of the screen.
    def test_draw_backgrounds(self):
        game = GuessingGameTest()
        restart_button = self.game.draw_backgrounds()
        self.assertEqual(restart_button.top, 500)
        self.assertEqual(restart_button.left, 10)

#It checks that the function correctly draws a board of 36 pieces, each of which is 50 pixels wide and high.
    def test_draw_board(self):
        game = GuessingGameTest()
        board_list = self.game.draw_board()
        self.assertEqual(len(board_list), 36)
        for piece in board_list:
            self.assertEqual(piece.width, 50)
            self.assertEqual(piece.height, 50)

#It checks that the function correctly marks the first two guesses as correct.
    def test_check_guesses(self):
        game = GuessingGameTest()
        game.check_guesses(0, 1)
        self.assertEqual(self.game.correct[0][0], 1)
        self.assertEqual(self.game.correct[0][1], 1)

