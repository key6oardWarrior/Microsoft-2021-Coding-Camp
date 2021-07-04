import pygame

ON_COLOR = (255,255,255)
OFF_COLOR = (40,40,40)
BORDER_COLOR = (0,0,0)
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
	return screen.fill(color,pygame.Rect(x*40 + 2,y*40 + 2,37,37))
	

def get_surround(x,y):
	out = 0

	if x > 0 and y > 0 and board[x-1][y-1]:
		out += 1
	if x > 0 and board[x-1][y]:
		out += 1
	if x > 0 and y < 9 and board[x-1][y+1]:
		out += 1
	if y < 9 and board[x][y+1]:
		out += 1
	if x < 9 and y < 9 and board[x+1][y+1]:
		out += 1
	if x < 9 and board[x+1][y]:
		out += 1
	if x < 9 and y > 0 and board[x+1][y-1]:
		out += 1
	if y > 0 and board[x][y-1]:
		out += 1

	return out


def update_cell(x,y):
	global next
	neighbors = get_surround(x,y)
	if board[x][y]: # if alive
		if neighbors < 2 or neighbors > 3:
			next[x][y] = False
		else:
			next[x][y] = True

	else: # if dead
		if neighbors == 3:
			next[x][y] = True
		else:
			next[x][y] = False

	return next[x][y]

def update_sim():
	global board
	global next
	rects = []

	for i in range(10):
		for j in range(10):
			alive = update_cell(i,j)
			rect = draw_cell(i,j,alive)
			rects.append(rect)
	board = [row[:] for row in next]
	pygame.display.update(rects)


pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

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
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			simulate = not simulate
		elif event.type == pygame.MOUSEBUTTONDOWN:
			square = (event.pos[0]//40,event.pos[1]//40)
			board[square[0]][square[1]] = not board[square[0]][square[1]]
			pygame.display.update(draw_cell(square[0],square[1],board[square[0]][square[1]]))
	if simulate:
		elapsed += clock.get_time()
		if elapsed >= DELAY:
			update_sim()
			elapsed = 0

