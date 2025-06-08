'''
Contains the Game class that handles the game logic for "Guess the Number".
'''
import random
class Game:
    def __init__(self):
        self.number_to_guess = self.generate_number()
        self.attempts = 0
        self.message = "Guess a number between 1 and 100!"
    def generate_number(self):
        return random.randint(1, 100)
    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.number_to_guess:
            self.message = "Too low! Try again."
        elif guess > self.number_to_guess:
            self.message = "Too high! Try again."
        else:
            self.message = f"Correct! You guessed it in {self.attempts} attempts."
            return True
        return False
    def reset_game(self):
        self.number_to_guess = self.generate_number()
        self.attempts = 0
        self.message = "Guess a number between 1 and 100!"