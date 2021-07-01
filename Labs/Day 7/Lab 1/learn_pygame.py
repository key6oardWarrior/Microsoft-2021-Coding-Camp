import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 1000
BACKGROUND_COLOR = (0, 0, 0) # black
FPS = 60 # frames per second
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BACKGROUND_COLOR)

isRunning = True

while isRunning:
	# teach how to get inputs after set up
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
		if((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
			isRunning = False

	# code for game play will go here
	window.blit(player, (playerPos[0], playerPos[1]))
	updatePlayer()

	# always the last lines of code to run to update the game screen
	pygame.display.flip()
	clock.tick(FPS)
	pygame.display.set_caption(f"FPS: {clock.get_fps()}")
