import pygame
from .constants import *

class Chest:
    def __init__(self, win):
        self.win = win
        self.chest_cards = list()
        self.chance_cards = list()
        self.init_chance_cards()
        self.init_chest_cards()
        pass

    def init_chance_cards(self):
        self.chest_cards.append("Advance to go!")
        pass

    def init_chest_cards(self):
        self.chance_cards.append("Advance to go!")
        pass

    def get_card(self, num, cchest):
        if cchest == True:
            return self.get_chest(num)
        elif cchest == False:
            return self.get_chance(num)

    def get_chance(self, num):
        return self.chance_cards[num - 1]

    def get_chest(self, num):
        ##print(num)
        return self.chest_cards[num - 1]