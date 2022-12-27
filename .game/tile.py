import pygame
from settings import tileScale

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, surf):
		super().__init__()
		self.image = pygame.transform.scale(surf, (tileScale, tileScale))
		self.rect = self.image.get_rect(topleft=pos)

	def update(self, worldShift):
		self.rect.x += worldShift