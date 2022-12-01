import pygame
from _objects.gameObject import gameObject
#adding functionality to our project

background_colour = (234, 212, 525)

screen = pygame.display.set_mode((300, 300))

pygame.display.set_caption('Platformer Game')

screen.fill(background_colour)

pygame.display.flip()

running = True

obiekt = gameObject(37, 21)
print(obiekt.posX)

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
