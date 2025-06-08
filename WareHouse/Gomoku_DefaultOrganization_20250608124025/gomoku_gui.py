'''
Contains the GUI for the Gomoku game.
'''
import tkinter as tk
from tkinter import messagebox
class GomokuGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        self.create_widgets()
        self.status_label = tk.Label(master, text="Current Player: X")
        self.status_label.grid(row=15, column=0, columnspan=15)
    def create_widgets(self):
        for row in range(15):
            for col in range(15):
                button = tk.Button(self.master, text="", width=4, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def on_button_click(self, row, col):
        self.game.make_move(row, col)
        self.update_board()
        if self.game.winner:
            self.update_status(f"Player {self.game.winner} wins!")
            messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
            self.game.reset_game()
            self.update_board()
    def update_board(self):
        for row in range(15):
            for col in range(15):
                if self.game.board[row][col] is not None:
                    self.buttons[row][col].config(text=self.game.board[row][col])
        self.update_status(f"Current Player: {self.game.current_player}")
    def update_status(self, message):
        self.status_label.config(text=message)