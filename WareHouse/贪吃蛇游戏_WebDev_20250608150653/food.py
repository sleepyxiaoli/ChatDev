'''
Contains the Food class for the Snake game.
'''
import pygame
import random
class Food:
    def __init__(self):
        self.randomize_position()
    def randomize_position(self):
        self.position = (random.randint(0, 59), random.randint(0, 39))
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.position[0] * 10, self.position[1] * 10, 10, 10))