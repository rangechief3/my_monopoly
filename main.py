import pygame

from Classes.constants import *
from Classes.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly")
pygame.init()

def main():
    running = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    game.buttons[0].draw()
    while running:
        clock.tick(FPS)
        running = game.game_cycle()

   # while running:
        #clock.tick(FPS)
            #for event in pygame.event.get():
         #   if event.type == pygame.QUIT:
        #        running = False
       #     if event.type == pygame.MOUSEBUTTONDOWN:
      #          pos = pygame.mouse.get_pos()
     #           game.select(pos)
    #    pygame.display.update()

    pygame.quit()
    

main()