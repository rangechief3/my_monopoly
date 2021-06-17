import pygame

from .constants import *

class Player:
    def __init__(self, win, name):
        self.position = 0
        self.name = name

    def __str__(self) -> str:
        return self.name