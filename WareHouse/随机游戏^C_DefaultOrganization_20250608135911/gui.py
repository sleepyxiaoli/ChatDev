'''
Contains the GUI class that handles the graphical user interface for the game.
'''
import pygame
class GUI:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.Font(None, 36)
        self.input_box = pygame.Rect(100, 100, 140, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.active = False
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.text.isdigit():
                        guess = int(self.text)
                        if self.game.check_guess(guess):
                            self.reset_input()
                    else:
                        self.game.message = "Please enter a valid number."
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
    def reset_input(self):
        self.text = ''
        self.game.reset_game()
    def draw(self):
        self.screen.fill((30, 30, 30))
        txt_surface = self.font.render(self.text, True, self.color)
        width = max(200, txt_surface.get_width()+10)
        self.input_box.w = width
        self.screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
        pygame.draw.rect(self.screen, self.color, self.input_box, 2)
        message_surface = self.font.render(self.game.message, True, (255, 255, 255))
        self.screen.blit(message_surface, (20, 150))