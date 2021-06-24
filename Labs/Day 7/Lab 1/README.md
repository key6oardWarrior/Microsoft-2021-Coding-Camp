<!DOCTYPEhtml>
 <html>
  <body>

<h1>Pygame Basics</h1>
<ol>
	<li>How to use Pygame:<br />
	Step one is to import the pygame module. Type:<br /> <code>import pygame<br />from pygame.locals import *</code></li>
	<li>Then, the first line of code from pygame that must be run is the initialize (aka init) function. Type:<br />
	<code>pygame.init()</code></li>
	<li>Set a few const vars:<br />
	<code>BACKGROUND_COLOR = (255, 255, 255) # white</br />
	FPS = 60<br />WIDTH = 400<br />HEIGHT = 300<br />
	clock = pygame.time.Clock()</code><br />
	This will allow us to control the size of our game window and the frames per second (FPS) of our game.</li>
	<li>We will now need a game window for the game to be played in. Type<br /><code>WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))</code></li>
	<li>Next, we will need a main loop for the game. This loop will contine to run as long as game needs to be played. For example, while game_is_running == True:<br /># code that will keep game running. Type:<br />
	<code>isRunning = True<br />while isRunning:<br />
	&#8195;&#8195;&#8195;&#8195;WINDOW.fill(BACKGROUND_COLOR)<br />&#8195;&#8195;&#8195;&#8195;pygame.display.update()<br />&#8195;&#8195;&#8195;&#8195;clock.tick(FPS)</code></li>
</ol>

 </body>
</html>