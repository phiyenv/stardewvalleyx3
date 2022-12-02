import pygame, sys 
from settings import *
from level import Level

class Game:

    def __init__(self):
        pygame.init () # Initialization
        # attributes
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Yoga Surf Land')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            # Checking if we are closing the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() # Close the game

            dt = self.clock.tick() / 1000 # datatime
            self.level.run(dt)
            pygame.display.update()

# Checking if we are in the main file
if __name__ == '__main__':
    game = Game ()
    game.run()