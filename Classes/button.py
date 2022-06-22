import pygame
from .constants import *

class Button:
    def __init__(self, win, text, x, y, drawable, clickable) -> None:
        self.win = win
        self.text = text
        self.x = x
        self.y = y
        self.drawable = drawable
        self.clickable = clickable
        self.draw()

    def draw(self):
        if self.drawable:
            x = self.x
            y = self.y
            pygame.draw.rect(self.win, BLACK, (x, y, button_width, button_height), 0, 7)
            pygame.draw.rect(self.win, BOARD_COLOR, (x + Buff, y + Buff, button_width - 2 * Buff, button_height - 2 * Buff), 0, 3)
        
            butText = self.text
            font = pygame.font.SysFont('Arial', 20)
            text = font.render(butText, 1, BLACK)
            self.win.blit(text, ((self.x + button_width // 2) - text.get_width() // 2, (self.y + button_height // 2) - text.get_height()//2))