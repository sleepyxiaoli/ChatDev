'''
Main file to run the Guess the Number game.
'''
from game import Game
from game_app import GameApp
import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Guess the Number Game")
    app = GameApp(root, Game())
    root.mainloop()
if __name__ == "__main__":
    main()