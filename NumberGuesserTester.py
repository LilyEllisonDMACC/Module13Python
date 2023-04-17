"""
Program: NumberGuesserTester.py
Author: Lily Ellison
Last date modified: 04/17/2023

The purpose of this program is to test the NumberGuesser class.

"""

import unittest
import gui_number_game as gng


class NumberGuessTester(unittest.TestCase):
    def test_setUp(self):
        self.num_guess = gng.NumberGuesser()

    def test_constructor(self):
        self.num_guess = gng.NumberGuesser()
        self.assertIsNotNone(len(self.num_guess.guessed_list))

    def test_adding_guessed_list(self):
        self.num_guess = gng.NumberGuesser()
        self.num_guess.add_guess(1)
        self.assertEqual(1, len(self.num_guess.guessed_list))

    def tearDown(self) -> None: ...


if __name__ == '__main__':
    unittest.main()
