'''
This module contains the Game class that manages the game logic.
'''
import random
class Game:
    def __init__(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.random_number:
            return "Too low!"
        elif guess > self.random_number:
            return "Too high!"
        else:
            return f"Correct! It took you {self.attempts} attempts."
    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0