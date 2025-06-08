'''
SudokuApp class to create the GUI for the Sudoku application.
'''
import tkinter as tk
from tkinter import messagebox
from sudoku_solver import SudokuSolver
class SudokuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()
    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j] = tk.Entry(self.master, width=2, font=('Arial', 24), justify='center')
                self.entries[i][j].grid(row=i, column=j)
        solve_button = tk.Button(self.master, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=10, column=0, columnspan=9)
        reset_button = tk.Button(self.master, text="Reset", command=self.reset_board)
        reset_button.grid(row=11, column=0, columnspan=9)
    def solve_sudoku(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit() and 1 <= int(value) <= 9:
                    self.board[i][j] = int(value)
                else:
                    self.board[i][j] = 0
        solver = SudokuSolver()
        if solver.solve(self.board):
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.board[i][j]))
        else:
            messagebox.showinfo("Error", "No solution exists!")
    def reset_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.board[i][j] = 0