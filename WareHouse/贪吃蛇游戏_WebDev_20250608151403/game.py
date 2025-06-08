'''
Class to manage the game logic and rendering.
'''
import pygame
from snake import Snake
from food import Food
class Game:
    def __init__(self):
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake()
        self.food = Food(self.width, self.height)
    def run(self):
        while self.running:
            self.handle_input()
            self.snake.move()
            if self.snake.check_collision(self.width, self.height):
                self.running = False
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.position = self.food.spawn(self.width, self.height)  # Update food position
            self.draw()
            self.clock.tick(15)
        self.display_score()
    def handle_input(self):
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
    def draw(self):
        self.screen.fill((0, 0, 0))
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], 10, 10))
        pygame.display.flip()
    def display_score(self):
        font = pygame.font.SysFont('Arial', 25)
        score_text = font.render(f'Score: {self.snake.get_score()}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before closing