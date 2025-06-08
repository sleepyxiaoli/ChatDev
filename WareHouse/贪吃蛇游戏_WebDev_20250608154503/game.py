'''
Game class that manages the game logic and rendering.
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
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
    def run(self):
        while not self.game_over:
            self.handle_events()
            self.snake.move()
            self.check_game_over()
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.spawn()
                self.score += 1
            self.draw()
            self.clock.tick(15)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    self.snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    self.snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.snake.direction = (1, 0)
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.display_score()
        pygame.display.flip()
    def display_score(self):
        font = pygame.font.SysFont("Arial", 25)
        score_surface = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))
    def check_game_over(self):
        head = self.snake.body[0]
        if head[0] < 0 or head[0] >= self.width or head[1] < 0 or head[1] >= self.height or head in self.snake.body[1:]:
            self.game_over = True