'''
This module defines the Food class, which manages the food's properties and position.
'''
import random
class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = (0, 0)
        self.randomize_position([])
    def randomize_position(self, snake_body):
        while True:
            self.position = (random.randint(0, (self.width // 10) - 1) * 10,
                             random.randint(0, (self.height // 10) - 1) * 10)
            if self.position not in snake_body:
                break
    def get_position(self):
        return self.position