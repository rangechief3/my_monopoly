import pygame

WIDTH = 1920
HEIGHT = 1000
board_width = 800

button_width = 100
button_height = 50

#13 slots per side of board
#9 of which are the middle pieces, 4 are the corner squares

Space_width = board_width // 13
Corner_width = Space_width * 2

Buff = 3
bar_buff = (Corner_width // 4) * 3
bar_width = Corner_width // 4 + 4

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
TEAL = (0, 255, 255)
BROWN = (101,67,35)
BLUE = (0, 0, 255)
RED = (255,0,0)
YELLOW = (255,255,0)
MAG = (204, 0 , 102)
ORANGE = (255,128,0)

BACKGROUND_COLOR = (0, 144, 48)
BOARD_COLOR = (194,220,202)

left_line = 600 + Corner_width
bot_line = 100 + Corner_width + Space_width * 9
right_line = 600 + Corner_width + Space_width * 9
top_line = 100 + Corner_width
