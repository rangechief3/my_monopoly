import pygame
import random
from .chest import Chest

class Property:
    def __init__(self, win, name, position):
        self.win = win
        self.cards = Chest(self.win)
        self.position = position
        #self.owner = -1
        self.price = -1
        self.name = name
        self.owned = False
        self.is_special = False
        self.init_price()
        self.set_chest()
        self.set_go()
        self.set_tax()
    
    def chest_turn(self):
        cchest = False
        if self.position == 2 or self.position == 17 or self.position == 33:
            cchest = True

        #cardNo = random.randint(1,16)
        #cardText = self.cards.get_card(cardNo, cchest)
        pass

    def set_go(self):
        if self.position == 0:
            self.go = True
        else:
            self.go = False

    def set_tax(self):
        if self.position == 4 or self.position == 38:
            self.tax = True
        else:
            self.tax = False

    def set_corner(self):
        self.jail = False
        self.free_parking = False
        self.go_to_jail = False
        if self.position == 10:
            self.jail = True
        elif self.position == 20:
            self.free_parking = True
        elif self.position == 30:
            self.go_to_jail = True


    def set_chest(self):
        if self.position == 2 or self.position == 7 or self.position == 17 or self.position == 22 or self.position == 33 or self.position == 36:
            self.chest = True
        else:
            self.chest = False

    def init_price(self):
        if self.position == 1 or self.position == 3:
            self.price = 60
        elif self.position == 6 or self.position == 8:
            self.price = 100
        elif self.position == 9:
            self.price = 120
        elif self.position == 11 or self.position == 13:
            self.price = 140
        elif self.position == 14:
            self.price = 160
        elif self.position == 16 or self.position == 18:
            self.price = 180
        elif self.position == 19:
            self.price = 200
        elif self.position == 21 or self.position == 23:
            self.price = 220
        elif self.position == 24:
            self.price = 240
        elif self.position == 26 or self.position == 27:
            self.price = 260
        elif self.position == 29:
            self.price = 280
        elif self.position == 31 or self.position == 32:
            self.price = 300
        elif self.position == 34:
            self.price = 320
        elif self.position == 37:
            self.price = 350
        elif self.position == 39:
            self.price = 400
        elif self.position == 4 or self.position == 5 or self.position == 15 or self.position == 25 or self.position == 35:
            self.price = 200
        elif self.position == 12 or self.position == 28:
            self.price = 150
        elif self.position == 38:
            self.price = 100
        else:
            self.price = -1
