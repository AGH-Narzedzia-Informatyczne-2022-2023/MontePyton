import pygame
from pytmx.util_pygame import load_pygame
from settings import tileScale
from player import Player
from tile import Tile

class Level:
    def __init__(self,path,screen):
        super().__init__()
        self.path = path
        self.screen = screen

        self.setupLevel()

    def setupLevel(self):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        player_sprite = Player((64, 64))
        self.player.add(player_sprite)

        tmxdata = load_pygame(self.path)

        for layer in tmxdata.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * tileScale, y * tileScale)
                    tile = Tile(pos, surf)
                    self.tiles.add(tile)

    def update(self):
        self.tiles.draw(self.screen)

        self.player.update()
        self.player.draw(self.screen)