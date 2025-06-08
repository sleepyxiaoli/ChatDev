'''
This module contains the SudokuGame class that handles the game logic,
including board generation, validation, and solving.
'''
import random
class SudokuGame:
    def __init__(self):
        self.board = [[0]*9 for _ in range(9)]
        self.generate_board()
    def generate_board(self):
        # Generate a complete Sudoku board
        self.fill_board()
        # Remove some numbers to create the puzzle
        self.remove_numbers()
    def fill_board(self):
        # Fill the board with a valid Sudoku solution
        self.solve()
    def is_valid_move(self, row, col, num):
        # Check if num can be placed at (row, col)
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        return True
    def solve(self):
        # Solve the Sudoku puzzle using backtracking
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True
    def remove_numbers(self):
        # Remove numbers from the board to create the puzzle
        count = 40  # Number of cells to remove
        while count > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1
    def reset(self):
        # Reset the game state
        self.board = [[0]*9 for _ in range(9)]
        self.generate_board()