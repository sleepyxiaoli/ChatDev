'''
Entry point of the Sudoku application.
'''
import tkinter as tk
from sudoku_app import SudokuApp
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()