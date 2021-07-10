import pygame
import os
import random

def shapes():
	# draw a line
	# args: game window, color, start point, end point, thickness
	COLOR = (255, 0, 0)
	pygame.draw.line(window, COLOR, (100, 100), (500, 7), 5)

	# draw polygon
	# ask students what is the last argument susposed to represent
	pygame.draw.polygon(window, COLOR, [(200, 200), (700, 688), (250, 321), (0, 0), (1, 5)])

	# last args are thickness and boundary
	pygame.draw.circle(window, COLOR, (300, 60), 50, 20)
	pygame.draw.circle(window, COLOR, (150, 150), 30)

	pygame.draw.rect(window, COLOR, pygame.Rect(100, 150, 200, 150))

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

def update(IMAGE, POS):
	'''
	Update the position of the image

	@param IMAGE - <class 'pygame.Surface'> user's image\n
	@param POS - <class 'list'> the image's new position
	'''
	window.blit(IMAGE, inBounds(POS[0], POS[1]))

def playerMovement():
	playerPos[0] += 10
	playerPos[1] += 10
	update(player, playerPos)

	# appear in random places without going off screen
	playerPos[0] = random.randint(0, WIDTH-PLAYER_WIDTH)
	playerPos[1] = random.randint(0, HEIGHT-PLAYER_HEIGHT)
	update(player, playerPos)

def show():
	global fps

	# display the game and the frame rate
	pygame.display.flip()
	# varable refresh rate
	clock.tick(fps)
	if fps < 60:
		fps = 200
	else:
		fps -= 10
	pygame.display.set_caption(f"FPS: {clock.get_fps()}")

pygame.init()
WIDTH = 600
HEIGHT = 700
BACKGROUND_COLOR = (0, 0, 0) # black
fps = 60 # frames per second
clock = pygame.time.Clock() # control FPS
window = pygame.display.set_mode((WIDTH, HEIGHT)) # game window
window.fill(BACKGROUND_COLOR) # set background color
isRunning = True

# player vars
playerPos = [0, 0]
player = display(f"{os.path.dirname(__file__)}\\assets\\BAX.png", playerPos)
PLAYER_WIDTH = player.get_width()
PLAYER_HEIGHT = player.get_height()

pygame.draw.line(window, (255,0,0), (100, 100), (300, 200), 5)

while isRunning:
	# event handling for ending the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
			break
		elif((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
			isRunning = False
			break
	
	shapes()
	playerMovement()
	show()