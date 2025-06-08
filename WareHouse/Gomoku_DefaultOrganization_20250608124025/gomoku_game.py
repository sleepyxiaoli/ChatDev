'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, row, col):
        if self.board[row][col] is None and self.winner is None:
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
    def check_winner(self):
        # Check horizontal, vertical, and diagonal lines for a win
        for row in range(15):
            for col in range(15):
                if self.board[row][col] is not None:
                    if self.check_direction(row, col, 1, 0) or \
                       self.check_direction(row, col, 0, 1) or \
                       self.check_direction(row, col, 1, 1) or \
                       self.check_direction(row, col, 1, -1):
                        return True
        return False
    def check_direction(self, row, col, delta_row, delta_col):
        count = 0
        for i in range(5):
            r = row + i * delta_row
            c = col + i * delta_col
            if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.board[row][col]:
                count += 1
            else:
                break
        return count == 5
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None