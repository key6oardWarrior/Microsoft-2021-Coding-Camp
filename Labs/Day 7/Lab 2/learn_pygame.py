import os
import pygame

def display(FILE_PATH, POSITION):
	'''
	@param FILE_PATH - <class 'str'> File path of the png image to be displayed\n
	@param POSITION - <class 'tuple'> the x and y position of the image\n
	@return <class 'pygame.Surface'> the image that the user wants to display
	'''
	global window

	image = pygame.image.load(FILE_PATH)
	image = pygame.transform.scale(image, (50, 50))
	window.blit(image, POSITION)
	
	return image

def updatePlayer():
	global playerPos
	KEY = pygame.key.get_pressed()
	
	if KEY[pygame.K_LEFT]:
		playerPos[0] -= 10
	elif KEY[pygame.K_RIGHT]:
		playerPos[0] += 10
	elif KEY[pygame.K_UP]:
		playerPos[1] -= 10
	elif KEY[pygame.K_DOWN]:
		playerPos[1] += 10

pygame.init()
WIDTH = 400
HEIGHT = 400
BACKGROUND_COLOR = (0, 0, 0) # black
FPS = 60 # frames per second
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BACKGROUND_COLOR)

playerPos = [0, 0]
# give the students this line of code
player = display(f"{os.path.dirname(__file__)}\\assets\\player.png", (playerPos[0], playerPos[1]))
isRunning = True

while isRunning:
	# teach how to get inputs after set up
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
		if((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
			isRunning = False

	# code for game play will go here
	updatePlayer()
	window.fill(BACKGROUND_COLOR)
	window.blit(player, (playerPos[0], playerPos[1]))

	# always the last lines of code to run to update the game screen
	pygame.display.flip()
	clock.tick(FPS)
	pygame.display.set_caption(f"FPS: {clock.get_fps()}")
