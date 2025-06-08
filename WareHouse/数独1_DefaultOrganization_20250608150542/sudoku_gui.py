'''
SudokuGUI class to manage the graphical user interface for the Sudoku application.
'''
import tkinter as tk
from tkinter import messagebox
from sudoku_solver import SudokuSolver
class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
        self.solve_button.grid(row=10, column=0, columnspan=9)
    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.master, width=2, font=('Arial', 24), justify='center')
                entry.grid(row=i, column=j)
                self.entries[i][j] = entry
    def update_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(grid[i][j]))
    def solve_sudoku(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                self.grid[i][j] = int(value) if value.isdigit() else 0
        solver = SudokuSolver(self.grid)
        if solver.solve():
            self.update_grid(solver.get_grid())
        else:
            messagebox.showinfo("Info", "No solution exists!")