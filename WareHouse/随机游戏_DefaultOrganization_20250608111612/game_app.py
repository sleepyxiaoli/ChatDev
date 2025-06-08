'''
This module contains the GameApp class that manages the GUI for the game.
'''
import tkinter as tk
from tkinter import messagebox
class GameApp:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_guess)
        self.submit_button.pack()
        self.message_label = tk.Label(master, text="")
        self.message_label.pack()
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.pack()
    def submit_guess(self):
        try:
            guess = int(self.entry.get())
            message = self.game.check_guess(guess)
            self.update_message(message)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
    def update_message(self, message):
        self.message_label.config(text=message)
    def reset_game(self):
        self.game.reset_game()
        self.message_label.config(text="Game has been reset! Guess a number between 1 and 100:")
        self.entry.delete(0, tk.END)