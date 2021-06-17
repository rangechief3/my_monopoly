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

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.quit()
    

main()