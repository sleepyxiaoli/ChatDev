'''
SudokuSolver class to handle the logic of solving the Sudoku puzzle.
'''
class SudokuSolver:
    def is_valid(self, board, row, col, num):
        # Check if num is not in the current row and column
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False
        # Check the 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True
    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:  # Empty cell
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            board[row][col] = 0  # Backtrack
                    return False
        return True