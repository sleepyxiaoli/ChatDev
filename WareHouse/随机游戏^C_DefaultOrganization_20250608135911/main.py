'''
Main entry point for the Guess the Number game.
'''
import pygame
from gui import GUI
from game import Game
def run():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Guess the Number Game")
    game = Game()
    gui = GUI(screen, game)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            gui.handle_event(event)
        gui.draw()
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    run()