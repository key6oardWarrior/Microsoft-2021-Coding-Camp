import os
import pygame

def inBounds(x, y):
	'''
	Return a tuple that is in bounds of the game window

	@param x - <class 'int'> x value of image\n
	@param y - <class 'int'> y value of image\n
	@return <class 'tuple'> the x and y that is in bounds of the game window
	'''

	if x > HEIGHT:
		x = HEIGHT - PLAYER_HEIGHT
	
	if y > WIDTH:
		y = WIDTH - PLAYER_WIDTH
	
	return (x, y)

def display(FILE_PATH, POS):
	'''
	Display the image that the user wants displayed

	@param FILE_PATH - <class 'str'> path of the user's image\n
	@param POS - <class 'tuple'> the player image's position\n
	@return <class 'pygame.Surface'> the user's image
	'''
	image = pygame.image.load(FILE_PATH)
	image = pygame.transform.scale(image, (50, 50)) # scale the image down or up
	window.blit(image, inBounds(POS[0], POS[1]))

	return image

pygame.init()
WIDTH = 600
HEIGHT = 700
BACKGROUND_COLOR = (0, 0, 0) # black
FPS = 60 # frames per second
clock = pygame.time.Clock() # control FPS
window = pygame.display.set_mode((WIDTH, HEIGHT)) # game window
window.fill(BACKGROUND_COLOR) # set background color
isRunning = True

# player vars
playerPos = [0, 100]
player = display(f"{os.path.dirname(__file__)}\\assets\\BAX.png", playerPos)
PLAYER_WIDTH = player.get_width()
PLAYER_HEIGHT = player.get_height()

while isRunning:
	# event handling for ending the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
			break
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				isRunning = False
				break
			elif event.key == pygame.K_UP:
				playerPos[1] -= 50
			elif event.key == pygame.K_DOWN:
				playerPos[1] += 50

	window.blit(player, inBounds(playerPos[0], playerPos[1]))
	pygame.display.set_caption(f"FPS: {clock.get_fps()}")

	pygame.display.flip()
	clock.tick(FPS)
	pygame.display.update()