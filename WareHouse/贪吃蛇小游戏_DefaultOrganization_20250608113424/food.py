'''
Class representing the Food in the game.
'''
import pygame
import random
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()
    def spawn(self):
        self.position = (random.randint(0, 59) * 10, random.randint(0, 39) * 10)
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(self.position[0], self.position[1], 10, 10))