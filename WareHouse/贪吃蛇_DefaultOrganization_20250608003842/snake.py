'''
This module defines the Snake class, which manages the snake's properties and behavior.
'''
import pygame
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)  # Start moving to the right
        self.length = 3
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        if len(self.body) > self.length:
            self.body.pop()
    def grow(self):
        self.length += 1
    def get_head_position(self):
        return self.body[0]
    def get_body(self):
        return self.body