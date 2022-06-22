import pygame

from .constants import *
from .property import *

class Player:
    def __init__(self, win, name, color):
        self.position = 0
        self.color = color
        self.win = win
        self.name = name
        self.in_jail = False
        self.money = 1500
        self.jail_turns = 0
        self.properties = list()

    def add_property(self, property):
        self.properties.append(property)

        #for i, prop in enumerate(self.properties):
            #print(prop.name)

    def get_taxed(self, amount):
        self.money -= amount
        

    def display_taxed(self, amount):
        taxText = "You were taxed: " + str(amount)

        pygame.draw.rect(self.win, BLACK, (100, 200, 200, 50), 0, 7)
        pygame.draw.rect(self.win, WHITE, (100 + Buff, 200 + Buff, 200 - 2 * Buff, 50 - 2 * Buff), 0, 3)

        font = pygame.font.SysFont('Arial', 20)
        text = font.render(taxText, 1, BLACK)
        self.win.blit(text, ((100 + (200 + Buff) // 2) - text.get_width() // 2, (200 + (50 + Buff) // 2) - text.get_height() // 2))
        pygame.display.update()

    def just_visiting(self):
        visitingText = "Just visiting"
        pygame.draw.rect(self.win, BLACK, (100, 200, 100, 50), 0, 7)
        pygame.draw.rect(self.win, WHITE, (100 + Buff, 200 + Buff, 100 - 2 * Buff, 50 - 2 * Buff), 0, 3)

        font = pygame.font.SysFont('Arial', 20)
        text = font.render(visitingText, 1, BLACK)
        self.win.blit(text, ((100 + (100 + Buff) // 2) - text.get_width() // 2, (200 + (50 + Buff) // 2) - text.get_height() // 2))
        pygame.display.update()       

    def go_to_jail(self):
        self.in_jail = True
        self.position = 10

    def display_jail(self):
        jailText = "Go to jail!"
        pygame.draw.rect(self.win, BLACK, (100, 200, 100, 50), 0, 7)
        pygame.draw.rect(self.win, WHITE, (100 + Buff, 200 + Buff, 100 - 2 * Buff, 50 - 2 * Buff), 0, 3)

        font = pygame.font.SysFont('Arial', 20)
        text = font.render(jailText, 1, BLACK)
        self.win.blit(text, ((100 + (100 + Buff) // 2) - text.get_width() // 2, (200 + (50 + Buff) // 2) - text.get_height() // 2))
        pygame.display.update() 

    def jail_turn(self):
        turnText = "This is jail turn " + str(self.jail_turns + 1)

        pygame.draw.rect(self.win, BLACK, (100, 200, 200, 50), 0, 7)
        pygame.draw.rect(self.win, WHITE, (100 + Buff, 200 + Buff, 200 - 2 * Buff, 50 - 2 * Buff), 0, 3)

        font = pygame.font.SysFont('Arial', 20)
        text = font.render(turnText, 1, BLACK)
        self.win.blit(text, ((100 + (200 + Buff) // 2) - text.get_width() // 2, (200 + (50 + Buff) // 2) - text.get_height() // 2))
        
        self.jail_turns += 1

        if self.jail_turns == 3:
            self.in_jail = False
            self.jail_turns = 0

    def land_go(self):
        self.money += 400

    def pass_go(self):
        self.money += 200

    def display_go(self):
        if self.position == 0:
            goText = "You landed on go! Collect 400 dollars!"
            y = 200
        else:
            goText = "You passed go! Collect 200 dollars!"
            y = 100

        pygame.draw.rect(self.win, BLACK, (100, y, 300, 50), 0, 7)
        pygame.draw.rect(self.win, WHITE, (100 + Buff, y + Buff, 300 - 2 * Buff, 50 - 2 * Buff), 0, 3)

        font = pygame.font.SysFont('Arial', 20)
        text = font.render(goText, 1, BLACK)
        self.win.blit(text, ((100 + (300 + Buff) // 2) - text.get_width() // 2, (y + (50 + Buff) // 2) - text.get_height() // 2))
        pygame.display.update()

    def free_parking(self):
        freeText = "Free Parking"
        pygame.draw.rect(self.win, BLACK, (100, 200, 200, 50), 0, 7)
        pygame.draw.rect(self.win, WHITE, (100 + Buff, 200 + Buff, 200 - 2 * Buff, 50 - 2 * Buff), 0, 3)

        font = pygame.font.SysFont('Arial', 20)
        text = font.render(freeText, 1, BLACK)
        self.win.blit(text, ((100 + (200 + Buff) // 2) - text.get_width() // 2, (200 + (50 + Buff) // 2) - text.get_height() // 2))


    def draw(self, spot):
        pygame.draw.circle(self.win, BLACK, spot, 13)
        pygame.draw.circle(self.win, self.color, spot, 10)
        pygame.display.update()

    def display_stats(self):
        pygame.draw.rect(self.win, BLACK, (stats_x, 100, 200, 50), 0, 7)
        pygame.draw.rect(self.win, WHITE, (stats_x + Buff, 100 + Buff, 200 - 2 * Buff, 50 - 2 * Buff), 0, 3)
        moneyText = "Money: $" + str(self.money)

        font = pygame.font.SysFont('Arial', 20)
        text = font.render(moneyText, 1, BLACK)
        self.win.blit(text, (stats_x + 100 - text.get_width() // 2, 100 + 25 - text.get_height() // 2))

        pygame.display.update()

    def display_properties(self):
        pygame.draw.rect(self.win, BLACK, (stats_x, 200, 200, 300), 0, 7)
        pygame.draw.rect(self.win, WHITE, (stats_x + Buff, 200 + Buff, 200 - 2 * Buff, 300 - 2 * Buff), 0, 3)
        propText = "Properties:"
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(propText, 1, BLACK)
        self.win.blit(text, (stats_x + 2 * Buff, 200))

        if(len(self.properties) != 0):
            for i,property in enumerate(self.properties):
                propText = property.name
                font = pygame.font.SysFont('Arial', 20)
                text = font.render(propText, 1, BLACK)
                self.win.blit(text, (stats_x + 2 * Buff, 200 + (i + 1) * text.get_height()))

        pygame.display.update()

    def __str__(self) -> str:
        return self.name