"""
This code defines a class called "Player" that is a child class of pygame.sprite.Sprite, 
which is a Pygame module for creating sprites (moving images) in a game.
The class has four methods: __init__, input, move, and update.

The __init__ method is called when an instance of the class is created. It takes two arguments pos and group, 
it creates an instance of the Sprite and assigns it to the group passed as a parameter. It also creates a pink 
colored surface of size 32x64 pixels, and creates a rect object that is centered at the position passed as a 
parameter. It also creates two attributes, speed and direction which are used for movement, and pos a Vector2 object of Pygame.

The input method is used to handle the inputs from the player by reading the keyboard state, it checks if the up, down, 
left or right keys are pressed and sets the direction attribute accordingly.

The move method is used to move the sprite based on the direction and speed attributes, it updates the position of the 
sprite by adding the product of direction, speed and the time passed since the last frame update (dt) to the current 
position of the sprite.

The update method is used to call the input method and update the sprite based on the inputs.

This class is using settings module, which contain the settings for the game.

"""

import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)

		# general setup
		self.image = pygame.Surface((32,64))
		self.image.fill('pink')
		self.rect = self.image.get_rect(center = pos)

		# movement attributes
		self.speed = 200
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		#print(self.direction)	
		# "dt" represents the elapsed time since the last frame update

	def move(self,dt):

		# normalizing a vector 
		"""The first step in the method is to normalize the direction vector. This is done by dividing the vector by its magnitude. 
		This ensures that the direction vector has a length of 1, which is important for ensuring that the player moves at a 
		consistent speed."""
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		"""The next step is to update the player's position. The x and y components of the position vector are both incremented 
		by the corresponding components of the direction vector, multiplied by the player's speed and dt. This will move the player
		in the direction specified by the direction vector, at a speed of "speed" units per second. 
		Finally, the rect's centerx and centery attributes are set to the player's x and y position respectively, to reflect the
		change in position."""
		# horizontal movement                                                          
		self.pos.x += self.direction.x * self.speed * dt                                                                                             
		self.rect.centerx = self.pos.x
		# vertical movement
		self.pos.y += self.direction.y * self.speed * dt
		self.rect.centery = self.pos.y

	def update(self,dt):
		self.input()
		self.move(dt)


