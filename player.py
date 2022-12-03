import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)

        self.image = pygame.Surface((64,32))
        self.image.fill('green')
        self.rectangle = self.image.get_rectangle(center = position)
