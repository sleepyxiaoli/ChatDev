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
        self.score = 0
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.snake.move()
            if self.check_collision():
                self.running = False
            if self.snake.get_head_position() == self.food.position:
                self.snake.grow()
                self.food.randomize_position()
                self.update_score()
            self.draw()
            self.clock.tick(10)
        self.game_over()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                    self.snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                    self.snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                    self.snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                    self.snake.direction = (1, 0)
    def check_collision(self):
        head_x, head_y = self.snake.get_head_position()
        if head_x < 0 or head_x >= self.width // 10 or head_y < 0 or head_y >= self.height // 10:
            return True
        return head_x, head_y in self.snake.body[1:]
    def update_score(self):
        self.score += 1
        print(f"Score: {self.score}")
    def draw(self):
        self.window.fill((0, 0, 0))
        self.snake.draw(self.window)
        self.food.draw(self.window)
        pygame.display.flip()
    def game_over(self):
        print(f"Game Over! Your final score is: {self.score}")
        pygame.quit()
if __name__ == "__main__":
    game = Game()
    game.run()