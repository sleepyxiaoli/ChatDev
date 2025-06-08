'''
This module contains the Minesweeper game logic and GUI implementation.
'''
import tkinter as tk
import random
class MinesweeperGame:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.setup_board()
    def setup_board(self):
        # Place mines randomly
        mines_placed = 0
        while mines_placed < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == -1:
                continue
            self.board[y][x] = -1
            mines_placed += 1
            # Update surrounding cells
            for i in range(max(0, y - 1), min(self.height, y + 2)):
                for j in range(max(0, x - 1), min(self.width, x + 2)):
                    if self.board[i][j] != -1:
                        self.board[i][j] += 1
    def reveal_cell(self, x, y):
        if self.game_over or self.revealed[y][x]:
            return
        self.revealed[y][x] = True
        if self.board[y][x] == -1:
            self.game_over = True
            return
        if self.board[y][x] == 0:
            for i in range(max(0, y - 1), min(self.height, y + 2)):
                for j in range(max(0, x - 1), min(self.width, x + 2)):
                    self.reveal_cell(j, i)
    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and self.board[y][x] != -1:
                    return False
        return True
    def reset_game(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.revealed = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.game_over = False
        self.setup_board()
class MinesweeperGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Minesweeper")
        self.game = MinesweeperGame(10, 10, 10)
        self.buttons = [[None for _ in range(self.game.width)] for _ in range(self.game.height)]
        self.create_widgets()
    def create_widgets(self):
        for y in range(self.game.height):
            for x in range(self.game.width):
                button = tk.Button(self.master, text='', width=3, command=lambda x=x, y=y: self.cell_clicked(x, y))
                button.grid(row=y, column=x)
                self.buttons[y][x] = button
    def cell_clicked(self, x, y):
        self.game.reveal_cell(x, y)
        self.update_board()
        if self.game.game_over:
            self.show_message("Game Over!")
        elif self.game.check_win():
            self.show_message("You Win!")
    def update_board(self):
        for y in range(self.game.height):
            for x in range(self.game.width):
                if self.game.revealed[y][x]:
                    if self.game.board[y][x] == -1:
                        self.buttons[y][x].config(text='*', bg='red')
                    else:
                        self.buttons[y][x].config(text=str(self.game.board[y][x]), bg='lightgrey')
    def show_message(self, message):
        message_box = tk.Toplevel(self.master)
        message_box.title("Message")
        tk.Label(message_box, text=message).pack()
        tk.Button(message_box, text="OK", command=message_box.destroy).pack()