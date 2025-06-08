'''
Module containing the Snake class.
'''
import pygame
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)  # Start moving to the right
        self.score = 0
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()
    def grow(self):
        # Instead of moving and then appending, just append a new segment
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)  # Add new head segment
        self.score += 1  # Increase score
    def check_collision(self, width, height):
        head_x, head_y = self.body[0]
        return (head_x < 0 or head_x >= width or head_y < 0 or head_y >= height or
                len(self.body) != len(set(self.body)))  # Check for wall collision and self-collision