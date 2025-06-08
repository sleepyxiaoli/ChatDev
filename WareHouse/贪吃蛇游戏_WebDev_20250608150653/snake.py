'''
Contains the Snake class for the Snake game.
'''
import pygame
class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)  # Start moving right
        self.grow_snake = False
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow_snake:
            self.body.pop()
        else:
            self.grow_snake = False
    def grow(self):
        self.grow_snake = True
    def get_head_position(self):
        return self.body[0]
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, (0, 255, 0), (segment[0] * 10, segment[1] * 10, 10, 10))