'''
Class representing the Food in the game.
'''
import random
class Food:
    def __init__(self, width, height):
        self.position = self.spawn(width, height)
    def spawn(self, width, height):
        x = random.randint(0, (width - 10) // 10) * 10
        y = random.randint(0, (height - 10) // 10) * 10
        return (x, y)