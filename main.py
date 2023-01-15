""" 
This code is a basic implementation of a game loop using the Pygame library in Python.
The code defines a class called "Game" which has two methods : "init" and "run".

The "init" method is called when an instance of the class is created. 
It initializes the Pygame library, sets up the game screen with a size and title,
creates a clock object to track the passage of time, and creates an instance of the "Level" class.

The "run" method contains a while loop that constantly updates the game screen. Within the loop, 
the code checks for a QUIT event (when the user closes the game window) and exits the game if one is detected. 
The method also calculates the amount of time that has passed since the last frame update using the clock object, 
passes this value to the "run" method of the "level" object and updates the screen.

The last line of code creates an instance of the "Game" class and starts the game loop.

"""

import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption('Cozy land')
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
  
			dt = self.clock.tick() / 1000
			self.level.run(dt)
			pygame.display.update()

# Game loop
if __name__ == '__main__':
	# Creates an instance of the Game class
	game = Game()
	# Calls the run method
	game.run()
