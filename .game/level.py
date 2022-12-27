import pygame
from pytmx.util_pygame import load_pygame
from settings import *
from player import Player
from tile import Tile

class Level:
    def __init__(self,path,screen):
        super().__init__()
        self.path = path
        self.screen = screen

        self.worldShift = 0.0

        self.setupLevel()

    def setupLevel(self):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        player_sprite = Player((300, 64))
        self.player.add(player_sprite)

        tmxdata = load_pygame(self.path)

        for layer in tmxdata.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * tileScale, y * tileScale)
                    tile = Tile(pos, surf)
                    self.tiles.add(tile)

    def moveCameraX(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 200 and direction_x < 0:
            self.worldShift = playerSpeed
            player.localSpeed = 0
        elif player_x > 1000 and direction_x > 0:
            self.worldShift = -playerSpeed
            player.localSpeed = 0
        else:
            self.worldShift = 0
            player.localSpeed = playerSpeed

    def update(self):
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.screen)

        self.player.update()
        self.player.draw(self.screen)
        self.moveCameraX()