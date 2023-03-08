# Imports
import pygame


# Sprite class tiles
class Block(pygame.sprite.Sprite):
    def __int__(self, pos, size):
        super().__int__()
        self.image = pygame.Surface((size, size))
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft=pos)

