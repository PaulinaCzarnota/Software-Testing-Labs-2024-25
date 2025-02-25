"""
Unit tests for the Wordle game.
"""
import unittest
from wordle import Wordle

class TestWordle(unittest.TestCase):
    def test_valid_word_length(self):
        with self.assertRaises(ValueError):
            Wordle("test")  # Too short
        with self.assertRaises(ValueError):
            Wordle("testing")  # Too long

    def test_game_over_after_six_attempts(self):
        game = Wordle("apple")
        for _ in range(6):
            game.guess("peach")
        self.assertTrue(game.game_over)

if __name__ == "__main__":
    unittest.main()