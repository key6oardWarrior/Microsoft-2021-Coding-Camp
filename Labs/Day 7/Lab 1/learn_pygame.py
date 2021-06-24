import pygame
from pygame.locals import *

pygame.init()

WIDTH = 400
HEIGHT = 300
BACKGROUND_COLOR = (255, 255, 255) # white
FPS = 60 # frames per second
clock = pygame.time.Clock()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

isRunning = True
while isRunning:
	# code for game play will go here

	# always the last lines of code to run to update the game screen
	WINDOW.fill(BACKGROUND_COLOR)
	pygame.display.update()
	clock.tick(FPS)