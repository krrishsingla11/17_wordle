import random
from words import WORDS
from feedback import evaluate

MAX_GUESSES = 6


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.words = [w for w in WORDS if len(w) == length]
        if not self.words:
            raise ValueError(f"No {length}-letter words in words.py. Add some to play this mode.")
        self.target = random.choice(self.words)
        self.history = []

    def validate(self, guess):
        """Return an error message, or None if the guess is OK."""
        if len(guess) != self.length:
            return f"Guess must be {self.length} letters long."
        if not guess.isalpha():
            return "Guess must contain letters only."
        if guess not in self.words:
            return "Not in the word list."
        return None

    def run(self):
        print(f"Wordle - {self.length} letters, {MAX_GUESSES} guesses. Type 'quit' to exit.")
        while len(self.history) < MAX_GUESSES:
            guess = input("> ").strip().lower()
            if guess == "quit":
                print("Thanks for playing!")
                return
            error = self.validate(guess)
            if error:
                print(error)
                continue
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            print(" ".join(feedback))
            if guess == self.target:
                print(f"You win! Solved in {len(self.history)}/{MAX_GUESSES} guesses.")
                return
        print(f"You lose! The word was: {self.target}")