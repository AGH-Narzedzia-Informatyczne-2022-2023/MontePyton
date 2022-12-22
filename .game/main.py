import pygame, sys
from pytmx.util_pygame import load_pygame
import player

r = 234
g = 212
b = 45

# 1 pixel = 4 x 4 pixels on screen
screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Platformer Game')

running = True

while running:

    background_colour = (r, g, b)

    screen.fill(background_colour)

    pygame.display.flip()

    obj = player.Player

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
