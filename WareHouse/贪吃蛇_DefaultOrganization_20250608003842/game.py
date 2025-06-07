'''
This module defines the Game class, which manages the game loop and overall game state.
'''
import pygame
from snake import Snake
from food import Food
class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food(self.width, self.height)
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.snake.move()
            self.check_collisions()
            self.draw_elements()
            self.clock.tick(15)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (0, 10):
                    self.snake.direction = (0, -10)
                elif event.key == pygame.K_DOWN and self.snake.direction != (0, -10):
                    self.snake.direction = (0, 10)
                elif event.key == pygame.K_LEFT and self.snake.direction != (10, 0):
                    self.snake.direction = (-10, 0)
                elif event.key == pygame.K_RIGHT and self.snake.direction != (-10, 0):
                    self.snake.direction = (10, 0)
    def draw_elements(self):
        self.window.fill((0, 0, 0))  # Clear the screen
        for segment in self.snake.get_body():
            pygame.draw.rect(self.window, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))
        food_position = self.food.get_position()
        pygame.draw.rect(self.window, (255, 0, 0), pygame.Rect(food_position[0], food_position[1], 10, 10))
        pygame.display.flip()
    def check_collisions(self):
        if self.snake.get_head_position() == self.food.get_position():
            self.snake.grow()
            self.food.randomize_position(self.snake.get_body())
        head_x, head_y = self.snake.get_head_position()
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            self.running = False
        for segment in self.snake.get_body()[1:]:
            if segment == self.snake.get_head_position():
                self.running = False