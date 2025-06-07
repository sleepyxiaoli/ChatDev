'''
Main entry point for the Snake game application.
'''
import pygame
from game import Game


def main():
    # width = int(input("请输入蛇可以活动的范围宽度: "))
    # height = int(input("请输入蛇可以活动的范围高度: "))
    pygame.init()
    game = Game(400, 300)
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
