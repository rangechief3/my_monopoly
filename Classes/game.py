from Classes.player import Player
from typing import List
import keyboard
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from .constants import *
from .board import Board
from .button import Button


class Game:
    def __init__(self, win):
        self.win = win
        self.board = Board(win)
        self.players = list()
        self.setup()
        
        
    def setup(self):
        settingUp = True
        numPlayers = -1
        x,y = -1, -1
        
        buttons = [Button(self.win, "2 Players", 100, 100)]
        buttons.append(Button(self.win, "3 Players", 200, 100))
        buttons.append(Button(self.win, "4 Players", 100, 150))
        buttons.append(Button(self.win, "5 Players", 200, 150))
        buttons.append(Button(self.win, "6 Players", 100, 200))
        buttons.append(Button(self.win, "7 Players", 200, 200))
        buttons.append(Button(self.win, "8 Players", 150, 250))
        pygame.display.update()
        while settingUp:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settingUp = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x,y = self.get_x_y(pos)
                    if x != -1 and y != -1:
                        for i,button in enumerate(buttons):
                            if(button.x <= x < button.x + button_width and button.y <= y < button.y + button_height):
                                numPlayers = i + 2
                                settingUp = False
        
        for i in range(0, numPlayers):
            self.add_player(i)
                            
    def add_player(self, index):
        name = ""
        if index == 0:
            name = "Scottie the Dog"
        elif index == 1:
            name = "The Top Hat"
        elif index == 2:
            name = "The Thimble"
        elif index == 3:
            name = "The Boot"
        elif index == 4:
            name = "The Wheelbarrow"
        elif index == 5:
            name = "The Cat"
        elif index == 6:
            name = "The Racecar"
        elif index == 7:
            name = "The Battleship"
        
        if len(name) != 0:
            self.players.append(Player(self.win, name))



    def get_x_y(self, pos):
        x = pos[0]
        y= pos[1]
        return x,y 