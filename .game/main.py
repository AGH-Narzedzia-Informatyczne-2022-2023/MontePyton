import pygame, sys
from level import Level
from settings import *

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))

Level = Level("../.game/gameinpy.tmx", screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    Level.update()

    pygame.display.update()