import pygame

ON_COLOR = (255,255,255) # White
OFF_COLOR = (40,40,40) # Dark Grey
BORDER_COLOR = (0,0,0) # Black
FPS = 60 # Framerate cap, in frames per second
DELAY = 100 # Delay, in milliseconds, between ticks of the simulation

board = [[False for i in range(10)] for j in range(10)] # Initialize a 10 x 10 matrix of Falses to represent the cells
next = [[False for i in range(10)] for j in range(10)] # Initialize another matrix to track the next iteration of the simulation


def draw_cell(x,y,alive):
	global screen
	if alive:
		color = ON_COLOR
	else:
		color = OFF_COLOR
	screen.fill(color,pygame.Rect(x*40 + 2,y*40 + 2,37,37))

def draw_board():
	for i in range(10):
		for j in range(10):
			alive = board[i][j]
			draw_cell(i,j,alive)

# Put any additional functions you write here

pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

# Draw the background and gridlines
screen.fill(OFF_COLOR)
for i in range(11):
	for j in range(11):
		pygame.draw.line(screen,BORDER_COLOR,(0,i*40),(400,i*40),3)
		pygame.draw.line(screen,BORDER_COLOR,(j*40,0),(j*40,400),3)
pygame.display.flip()

is_playing = True
simulate = False
elapsed = 0

while is_playing == True:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_playing = False
			break
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			is_playing = False
			break
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Toggle the simulation by pressing the space bar
			simulate = not simulate
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# TODO: use the attribute event.pos to change the "board" matrix in the right place,
			# corresponding to where on the screen the user clicks, in order to allow them to
			# change the status of cells by clicking on them. You can use draw_cell() to help, but remember
			# to update the screen to show the changes!
			
			
	if simulate:
		elapsed += clock.get_time() # Count the time spent processing the event queue
		
		if elapsed >= DELAY:
			# TODO: update the simulation here by calculating which cells will be
			# alive in the next step, and changing the "next" matrix to match.
			# A description of the rules behind Conway's game of life is included, and can also be found online.
			
			
			board = [row[:] for row in next] # Deep copy the elements from "next" into "board"
			draw_board() # Draw every cell on the board to the screen buffer
			pygame.screen.flip() # Display the buffer
			elapsed = 0

