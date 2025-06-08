'''
Class representing the Snake in the game.
'''
import pygame
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)  # Moving right
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()
    def grow(self):
        self.body.append(self.body[-1])  # Add a new segment at the tail
    def change_direction(self, x, y):
        self.direction = (x * 10, y * 10)
    @property
    def head(self):
        return self.body[0]
    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))