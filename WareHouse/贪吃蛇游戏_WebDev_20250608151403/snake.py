'''
Class representing the snake in the game.
'''
import pygame
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)
        self.score = 0
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        if len(self.body) > 1:
            self.body.pop()  # Remove the last segment unless growing
    def grow(self):
        self.body.append(self.body[-1])
        self.score += 1
    def check_collision(self, width, height):
        head_x, head_y = self.body[0]
        return (head_x < 0 or head_x >= width or 
                head_y < 0 or head_y >= height or 
                len(self.body) != len(set(self.body)))
    def get_score(self):
        return self.score