'''
Snake class that represents the snake in the game.
'''
import pygame
class Snake:
    def __init__(self):
        self.body = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)  # Start moving to the right
        self.speed = 10
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()  # Remove the tail
    def grow(self):
        self.body.append(self.body[-1])  # Add a new segment at the tail
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0] * self.speed, segment[1] * self.speed, self.speed, self.speed))
    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]  # Check if the head collides with the body