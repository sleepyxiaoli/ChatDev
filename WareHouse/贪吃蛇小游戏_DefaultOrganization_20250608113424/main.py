'''
Main file to run the Snake game.
'''
import pygame
from snake import Snake
from food import Food
class Game:
    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 400
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.snake.move()
            if self.check_collision():
                self.snake.grow()
                self.food.spawn()
            self.draw()
            self.clock.tick(10)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (0, 10):
                    self.snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN and self.snake.direction != (0, -10):
                    self.snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT and self.snake.direction != (10, 0):
                    self.snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT and self.snake.direction != (-10, 0):
                    self.snake.change_direction(1, 0)
    def check_collision(self):
        # Check for collision with food
        if self.snake.head == self.food.position:
            return True
        # Check for collision with itself
        if self.snake.head in self.snake.body[1:]:
            self.running = False  # End the game if the snake collides with itself
        # Check for collision with boundaries
        head_x, head_y = self.snake.head
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            self.running = False  # End the game if the snake goes out of bounds
        return False
    def draw(self):
        self.window.fill((0, 0, 0))
        self.snake.draw(self.window)
        self.food.draw(self.window)
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()