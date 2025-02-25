"""
Implementation of a simple Wordle game.
"""

class Wordle:
    def __init__(self, word):
        """Initialize Wordle game with a 5-letter word."""
        if len(word) != 5:
            raise ValueError("Word must be exactly 5 letters long.")
        self.word = word
        self.attempts = 0
        self.game_over = False

    def guess(self, word_guess):
        """Process a word guess."""
        if len(word_guess) != 5:
            raise ValueError("Guess must be exactly 5 letters long.")
        self.attempts += 1
        if word_guess == self.word:
            self.game_over = True
        elif self.attempts >= 6:
            self.game_over = True