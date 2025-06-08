'''
This module contains the SudokuGUI class that manages the graphical user interface
for the Sudoku game.
'''
import tkinter as tk
from tkinter import messagebox
from sudoku_game import SudokuGame
class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Game")
        self.game = SudokuGame()
        self.cells = [[None]*9 for _ in range(9)]
        self.create_board()
        self.update_board()
    def create_board(self):
        # Create the Sudoku grid in the GUI
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(self.master, width=2, font=('Arial', 24), justify='center')
                cell.grid(row=row, column=col, padx=5, pady=5)
                cell.bind("<FocusIn>", lambda e, r=row, c=col: self.on_cell_click(r, c))
                self.cells[row][col] = cell
    def update_board(self):
        # Update the displayed board
        for row in range(9):
            for col in range(9):
                value = self.game.board[row][col]
                self.cells[row][col].delete(0, tk.END)
                if value != 0:
                    self.cells[row][col].insert(0, str(value))
    def on_cell_click(self, row, col):
        # Handle cell click events
        value = self.cells[row][col].get()
        if value.isdigit() and 1 <= int(value) <= 9:
            if self.game.is_valid_move(row, col, int(value)):
                self.game.board[row][col] = int(value)
                self.update_board()
            else:
                messagebox.showerror("Invalid Move", "This move is not valid!")
    def show_solution(self):
        # Display the solution to the puzzle
        self.game.solve()
        self.update_board()
    def reset_game(self):
        # Reset the game in the GUI
        self.game.reset()
        self.update_board()