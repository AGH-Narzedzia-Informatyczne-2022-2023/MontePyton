import pygame, sys
from pytmx.util_pygame import load_pygame
from pathlib import Path
from player import Player

tileScale = 64

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(surf, (tileScale, tileScale))
        self.rect = self.image.get_rect(topleft = pos)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
tmxdata = load_pygame("../.game/gameinpy.tmx")
sprite_group = pygame.sprite.Group()

for layer in tmxdata.visible_layers:
    if hasattr(layer, 'data'):
        for x,y,surf in layer.tiles():
            print(surf)
            pos = (x * tileScale, y * tileScale)
            Tile(pos = pos, surf = surf, groups = sprite_group)

player = pygame.sprite.GroupSingle()
player_sprite = Player((64, 64))
player.add(player_sprite)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    sprite_group.draw(screen)

    player.update()
    player.draw(screen)

    pygame.display.update()