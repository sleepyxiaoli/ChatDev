'''
Module containing the Game class that manages the game logic.
'''
import pygame
from snake import Snake
from food import Food
class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.food = Food(width, height)
        self.game_over = False
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Snake Game')
    def run(self):
        clock = pygame.time.Clock()
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(15)  # Control the game speed
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (0, 10):
                    self.snake.direction = (0, -10)
                elif event.key == pygame.K_DOWN and self.snake.direction != (0, -10):
                    self.snake.direction = (0, 10)
                elif event.key == pygame.K_LEFT and self.snake.direction != (10, 0):
                    self.snake.direction = (-10, 0)
                elif event.key == pygame.K_RIGHT and self.snake.direction != (-10, 0):
                    self.snake.direction = (10, 0)
    def update(self):
        if not self.snake.check_collision(self.width, self.height):
            self.snake.move()  # Move only if no collision
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food = Food(self.width, self.height)
    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0], segment[1], 10, 10))
        food_x, food_y = self.food.position
        pygame.draw.rect(self.screen, (255, 0, 0), (food_x, food_y, 10, 10))
        # Display the score
        font = pygame.font.SysFont('Arial', 25)
        score_surface = font.render(f'Score: {self.snake.score}', True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))
        pygame.display.flip()  # Update the display