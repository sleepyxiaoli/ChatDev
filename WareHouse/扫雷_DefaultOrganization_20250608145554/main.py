'''
This is the main entry point for the Minesweeper application.
'''
import tkinter as tk
from minesweeper import MinesweeperGUI
def main():
    root = tk.Tk()
    app = MinesweeperGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()