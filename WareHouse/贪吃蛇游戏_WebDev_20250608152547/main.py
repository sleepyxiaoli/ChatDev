'''
Main file to run the Snake game.
'''
import pygame
from game import Game
def main():
    pygame.init()
    game = Game(800, 600)
    game.run()
    pygame.quit()
if __name__ == "__main__":
    main()