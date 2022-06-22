from Classes.player import Player
from typing import List
import keyboard
import pygame
import random
import time
from pygame.constants import MOUSEBUTTONDOWN
from .constants import *
from .board import Board
from .button import Button
from .property import Property



class Game:
    def __init__(self, win):
        self.win = win
        self.prev_pos = 0
        self.board = Board(win)
        self.curr_roll = 0
        self.players = list()
        self.player_turn = 0
        self.buttons = list()
        self.properties = list()
        self.buttons.append(Button(self.win, "Roll", 200, 200, True, False))
        self.board.draw()
        self.locations()
        self.setup()
        
    def game_cycle(self):
        selecting = True       
        self.board.draw()
        self.draw_players()
        self.buttons[0].drawable = True
        self.buttons[0].draw()
        self.buttons[0].drawable = False
        self.display_player()
        pygame.display.update()
        self.buttons[0].clickable = True
        while selecting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    selecting = False
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    selecting = self.select(pos)
                    if selecting == False:
                        self.buttons[0].clickable = False
                    #selecting = False            


        self.prev_pos = self.players[self.player_turn].position
        self.players[self.player_turn].position += self.curr_roll                        #########THIS IS THE ROLL
        self.players[self.player_turn].position = self.players[self.player_turn].position % 40


        #self.update_board()
        
        #self.display_landing(self.players[self.player_turn].position)
        
        self.take_a_turn()

        self.player_turn += 1
        self.player_turn = self.player_turn % self.numPlayers
        return True

    def take_a_turn(self):
        position = self.players[self.player_turn].position
        self.buttons[1].drawable = True
        self.buttons[2].drawable = True
        self.buttons[1].clickable = True
        self.buttons[2].clickable = True
        self.buttons[3].drawable = False
        self.buttons[3].drawable = False
        #self.draw_buttons()
        

        if self.prev_pos > self.players[self.player_turn].position and self.players[self.player_turn].position != 0:
            self.players[self.player_turn].pass_go()
            self.players[self.player_turn].display_go()
            time.sleep(1)
            

        if self.properties[position].tax == False and position % 10 != 0 and self.properties[position].chest == False and self.players[self.player_turn].in_jail == False:
            self.update_board()
            self.display_landing(self.players[self.player_turn].position)
            self.draw_buttons()
            selecting = True
            while selecting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        selecting = False
                        return False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        selecting = self.select(pos)
                        if selecting == False:
                            self.set_end_turn()
                            self.update_board()
                            self.draw_buttons()
        elif self.players[self.player_turn].in_jail == True:
            self.set_end_turn()
            self.players[self.player_turn].position = 10
            self.update_board()
            self.players[self.player_turn].jail_turn()
            self.draw_buttons()
        elif self.properties[position].tax == True:
            self.set_end_turn()
            self.players[self.player_turn].get_taxed(self.properties[position].price)
            self.update_board()
            self.players[self.player_turn].display_taxed(self.properties[position].price)
            self.draw_buttons()
        elif position % 10 == 0:
            if position == 0:
                self.set_end_turn()
                self.players[self.player_turn].land_go()
                self.update_board()
                self.players[self.player_turn].display_go()
                self.draw_buttons()
            elif position == 10:
                self.set_end_turn()
                self.update_board()
                self.players[self.player_turn].just_visiting()
                self.draw_buttons()
            elif position == 20:
                self.set_end_turn()                
                self.update_board()
                self.players[self.player_turn].free_parking()
                self.draw_buttons()
            elif position == 30:
                self.set_end_turn()
                self.players[self.player_turn].go_to_jail()
                self.update_board()
                self.players[self.player_turn].display_jail()
                self.draw_buttons()
        elif self.properties[position].chest == True:
                self.set_end_turn()
                self.properties[position].chest_turn()
                self.update_board()
                self.draw_buttons()
                         
        

        selecting = True
        while selecting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    selecting = False
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    selecting = self.select(pos)
    
    def set_end_turn(self):
                self.buttons[1].clickable = False
                self.buttons[2].clickable = False
                self.buttons[1].drawable = False
                self.buttons[2].drawable = False
                self.buttons[3].clickable = True
                self.buttons[3].drawable = True        

    def select(self, pos):
        x = pos[0]
        y = pos[1]

        for i, button in enumerate(self.buttons):
            if (button.x <= x < button.x + button_width and button.y <= y < button.y + button_height):
                if i == 0 and button.clickable:
                    self.board.draw()
                    self.roll_dice()
                    return False
                if i == 1 and button.clickable:
                    self.buy_property()
                    return False
                if i == 2 and button.clickable:
                    return False
                if i == 3 and button.clickable:
                    return False
        return True
    
    def roll_dice(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        rollTot = d1 + d2
        #
        # rollStr = "You rolled a " + str(rollTot)
        self.curr_roll = rollTot

    def buy_property(self):
        position = self.players[self.player_turn].position
        if self.players[self.player_turn].money >= self.properties[position].price and self.properties[position].owned == False:
            self.players[self.player_turn].money -= self.properties[position].price
            self.players[self.player_turn].add_property(self.properties[position])
            self.properties[position].owned = True
            #print(str(self.player_turn) + " " + str(self.players[self.player_turn].money))
        elif self.players[self.player_turn].money < self.properties[position].price:
            poorText = "You don't have enough money!"
            
            pygame.draw.rect(self.win, WHITE, (200, 200, 130, 50), 0 , 7)
            font = pygame.font.SysFont('Arial', 20)
            text = font.render(poorText, 1, BLACK)
            self.win.blit(text, ((200 + 130 // 2) - text.get_width() // 2, 225 - text.get_height() // 2))
            pygame.display.update()
            
###############################################################################################################################################################Setup stuff

    def setup(self):
        self.init_properties()
        self.init_buttons()
        settingUp = True
        numPlayers = -1
        x,y = -1, -1
        

        
        
        buttons = [Button(self.win, "1 Player", 150, 350, True, True)]
        buttons.append(Button(self.win, "2 Players", 100, 100, True, True))
        buttons.append(Button(self.win, "3 Players", 200, 100, True, True))
        buttons.append(Button(self.win, "4 Players", 100, 150, True, True))
        buttons.append(Button(self.win, "5 Players", 200, 150, True, True))
        buttons.append(Button(self.win, "6 Players", 100, 200, True, True))
        buttons.append(Button(self.win, "7 Players", 200, 200, True, True))
        buttons.append(Button(self.win, "8 Players", 150, 250, True, True))
        
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
                                numPlayers = i + 1
                                settingUp = False
        self.board.draw()
        pygame.display.update()
        self.numPlayers = numPlayers
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
            self.players.append(Player(self.win, name, piece_colors[index]))



    def get_x_y(self, pos):
        x = pos[0]
        y= pos[1]
        return x,y 

    def locations(self):
        bottomRow = 100 + 12 * Space_width
        topRow = 100 + Space_width
        leftCol = 600 + Space_width
        rightCol = 600 + 12 * Space_width
        self.locations = list()
        #self.locations.append((leftCol, bottomRow))
        for i in range(11):
            if i == 0:
                self.locations.append((leftCol, bottomRow - Space_width * i))    
            elif i == 10:
                self.locations.append((leftCol, bottomRow - Space_width * (1 + i)))
            else:
                self.locations.append((leftCol, bottomRow - Space_width * i - Space_width // 2))
        
        for i in range(10):
            if i == 9:
                self.locations.append((rightCol, topRow)) 
            else:
                self.locations.append((leftCol + Space_width * (i + 1) + Space_width // 2, topRow)) 

        for i in range(10):
            if i == 9:
                self.locations.append((rightCol, bottomRow))
            else:
                self.locations.append((rightCol, topRow + Space_width * (i + 1) + Space_width // 2)) 

        for i in range(9):
            self.locations.append((rightCol - Space_width * (i + 1) - Space_width // 2, bottomRow)) 

    def draw_players(self):
         for i, player in enumerate(self.players):
            player.draw(self.locations[self.players[i].position])       

    def init_properties(self):
        
        self.properties.append(Property(self.win, "Go", 0))
        self.properties.append(Property(self.win, "Mediterranean Avenue", 1))

        self.properties.append(Property(self.win, "Community Chest", 2))

        self.properties.append(Property(self.win, "Baltic Avenue", 3))
        self.properties.append(Property(self.win, "Income Tax", 4))
        self.properties.append(Property(self.win, "Reading Railroad", 5))
        self.properties.append(Property(self.win, "Oriental Avenue", 6))

        self.properties.append(Property(self.win, "Chance", 7))

        self.properties.append(Property(self.win, "Vermont Avenue", 8))
        self.properties.append(Property(self.win, "Connecticut Avenue", 9))

        self.properties.append(Property(self.win, "Jail", 10))

        self.properties.append(Property(self.win, "St. Charles Place", 11))
        self.properties.append(Property(self.win, "Electric Company", 12))
        self.properties.append(Property(self.win, "States Avenue", 13))
        self.properties.append(Property(self.win, "Virginia Avenue", 14))
        self.properties.append(Property(self.win, "Pennsylvania Railroad", 15))
        self.properties.append(Property(self.win, "St. James Place", 16))

        self.properties.append(Property(self.win, "Community Chest", 17))

        self.properties.append(Property(self.win, "Tennessee Avenue", 18))
        self.properties.append(Property(self.win, "New York Avenue", 19))

        self.properties.append(Property(self.win, "Free Parking", 20))

        self.properties.append(Property(self.win, "Kentucky Avenue", 21))

        self.properties.append(Property(self.win, "Chance", 22))

        self.properties.append(Property(self.win, "Indiana Avenue", 23))
        self.properties.append(Property(self.win, "Illinois Avenue", 24))
        self.properties.append(Property(self.win, "B & O Railroad", 25))
        self.properties.append(Property(self.win, "Atlantic Avenue", 26))
        self.properties.append(Property(self.win, "Ventnor Avenue", 27))
        self.properties.append(Property(self.win, "Water Works", 28))
        self.properties.append(Property(self.win, "Marvin Gardens", 29))

        self.properties.append(Property(self.win, "Go to Jail", 30))

        self.properties.append(Property(self.win, "Pacific Avenue", 31))
        self.properties.append(Property(self.win, "North Carolina Avenue", 32))

        self.properties.append(Property(self.win, "Community Chest", 33))

        self.properties.append(Property(self.win, "Pennsylvania Avenue", 34))
        self.properties.append(Property(self.win, "Short Line", 35))

        self.properties.append(Property(self.win, "Chance", 36))

        self.properties.append(Property(self.win, "Park Place", 37))
        self.properties.append(Property(self.win, "Luxury Tax", 38))
        self.properties.append(Property(self.win, "Boardwalk", 39))


    def update_board(self):
        self.board.draw()
        self.draw_players()
        self.players[self.player_turn].display_stats()
        self.players[self.player_turn].display_properties()

    def display_landing(self, position):
        landText = "You landed on " + self.properties[position].name

        font = pygame.font.SysFont('Arial', 20)
        text = font.render(landText, 1, BLACK)
        pygame.draw.rect(self.win, WHITE, (100, 200, 300, 50), 0 , 7)
        self.win.blit(text, ((100 + 300 // 2) - text.get_width() // 2, 225 - text.get_height() // 2))

        priceText = "This property is $" + str(self.properties[position].price)
        
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(priceText, 1, BLACK)
        pygame.draw.rect(self.win, WHITE, (100, 300, 300, 50), 0 , 7)
        self.win.blit(text, ((100 + 300 // 2) - text.get_width() // 2, 325 - text.get_height() // 2))
        
        pygame.display.update()

    def init_buttons(self):
        self.buttons.append(Button(self.win, "Buy", 100, 400, False, False))
        self.buttons.append(Button(self.win, "Pass", 200, 400, False, False))

        self.buttons.append(Button(self.win, "End Turn", 100, 600, False, False))
        pass
    
    def display_player(self):
        playerText = "Player " + str(self.player_turn + 1) + ", it's your turn"
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(playerText, 1, BLACK)
        pygame.draw.rect(self.win, WHITE, (100, 100, 300, 50), 0 , 7)
        self.win.blit(text, ((100 + 300 // 2) - text.get_width() // 2, 125 - text.get_height() // 2))
        pygame.display.update()

    def draw_buttons(self):
        for i,button in enumerate(self.buttons):
            button.draw()
        pygame.display.update()
