import pygame
from pygame import bufferproxy
from pygame import constants

from .constants import *

class Board:
    def __init__(self, win):
        self.win = win
        self.draw(self.win)

    def draw(self, win):
        self.win.fill(BACKGROUND_COLOR)
        pygame.draw.rect(self.win, BLACK, (600, 100, board_width, board_width))
        pygame.draw.rect(self.win, BOARD_COLOR, (600 + Buff, 100 + Buff, board_width - 2 * Buff, board_width - 2 * Buff))

                #Drawing left spaces

        #teal spaces
        pygame.draw.rect(self.win, TEAL, (600 + bar_buff, 100 + Corner_width, bar_width, Space_width))  
        pygame.draw.rect(self.win, TEAL, (600 + bar_buff, 100 + Corner_width + Space_width, bar_width, Space_width))
        pygame.draw.rect(self.win, TEAL, (600 + bar_buff, 100 + Corner_width + Space_width * 3, bar_width, Space_width))


        #brown spaces
        pygame.draw.rect(self.win, BROWN, (600 + bar_buff, 100 + Corner_width + Space_width * 6, bar_width, Space_width))
        pygame.draw.rect(self.win, BROWN, (600 + bar_buff, 100 + Corner_width + Space_width * 8, bar_width, Space_width))

        #lines
        pygame.draw.line(self.win, BLACK, (600 + Corner_width, 100),(600 + Corner_width, 100 + board_width - 1), 2)
        for i in range(0, 10):
            pygame.draw.line(self.win, BLACK, (600, 100 + Corner_width + Space_width * i),(left_line, 100 + Corner_width + Space_width * i), 2)

        
                #Drawing bottom spaces
        
        #blue spaces

        pygame.draw.rect(self.win, BLUE, (600 + Corner_width, bot_line, Space_width, bar_width))
        pygame.draw.rect(self.win, BLUE, (600 + Corner_width + Space_width * 2, bot_line, Space_width, bar_width))

        #green spaces

        pygame.draw.rect(self.win, GREEN, (600 + Corner_width + Space_width * 5, bot_line, Space_width, bar_width))
        pygame.draw.rect(self.win, GREEN, (600 + Corner_width + Space_width * 7, bot_line, Space_width, bar_width))
        pygame.draw.rect(self.win, GREEN, (600 + Corner_width + Space_width * 8, bot_line, Space_width, bar_width))

        #lines
        
        pygame.draw.line(self.win, BLACK,(600, bot_line),(600 + board_width - 1, bot_line), 2)
        for i in range(0,10):
            pygame.draw.line(self.win, BLACK, (600 + Corner_width + Space_width * i, bot_line), (600 + Corner_width + Space_width * i, bot_line + Corner_width + 4), 2)

            #Drawing right spaces

        #red spaces

        pygame.draw.rect(self.win, RED, (right_line, 100 + Corner_width, bar_width, Space_width))
        pygame.draw.rect(self.win, RED, (right_line, 100 + Corner_width + Space_width * 2, bar_width, Space_width))
        pygame.draw.rect(self.win, RED, (right_line, 100 + Corner_width + Space_width * 3, bar_width, Space_width))

        #yellow spaces

        pygame.draw.rect(self.win, YELLOW, (right_line, 100 + Corner_width + Space_width * 5, bar_width, Space_width))
        pygame.draw.rect(self.win, YELLOW, (right_line, 100 + Corner_width + Space_width * 6, bar_width, Space_width))
        pygame.draw.rect(self.win, YELLOW, (right_line, 100 + Corner_width + Space_width * 8, bar_width, Space_width))

        #lines

        pygame.draw.line(self.win, BLACK,(right_line, 100 + board_width),(right_line, 100), 2)
        for i in range(0, 10):
            pygame.draw.line(self.win, BLACK,(right_line, bot_line - (Space_width * i)), (600 + board_width, bot_line - (Space_width * i)), 2)    

            #Drawing top spaces

        #mag spaces

        pygame.draw.rect(self.win, MAG, (600 + Corner_width, 100 + bar_buff, Space_width, bar_width))
        pygame.draw.rect(self.win, MAG, (600 + Corner_width + Space_width * 2, 100 + bar_buff, Space_width, bar_width))
        pygame.draw.rect(self.win, MAG, (600 + Corner_width + Space_width * 3, 100 + bar_buff, Space_width, bar_width))
        
        #orange spaces

        pygame.draw.rect(self.win, ORANGE, (600 + Corner_width + Space_width * 5, 100 + bar_buff, Space_width, bar_width))
        pygame.draw.rect(self.win, ORANGE, (600 + Corner_width + Space_width * 7, 100 + bar_buff, Space_width, bar_width))
        pygame.draw.rect(self.win, ORANGE, (600 + Corner_width + Space_width * 8, 100 + bar_buff, Space_width, bar_width))

        #lines

        pygame.draw.line(self.win, BLACK, (600, 100 + Corner_width), (600 + board_width, 100 + Corner_width), 2)
        for i in range(0, 10):
            pygame.draw.line(self.win, BLACK, (600 + Corner_width + Space_width * i, 100), (600 + Corner_width + Space_width * i, top_line), 2)

        pygame.display.update()