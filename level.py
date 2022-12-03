import pygame 
from settings import *
from player import Player 

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

    def setup (self):
        self.player = Player((640,260), self.all_sprites) 
        # Player((640,260), self.all_sprites) = Player ((x,y),group) = Player (position,group)

    def run(self,dt):
        self.display_surface.fill('pink')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()

