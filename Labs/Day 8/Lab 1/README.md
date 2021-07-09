# Conway's Game of Life

The object of this lab will be to use more advanced pygame tools to implement Conway's Game of Life, a well-known cellular automaton.

## The Game

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a set of rules which governs how a square grid of cells evolves from initial conditions. Each cell can be either "alive" or "dead," and whether a cell is alive or dead in the next generation depends on how many of its neighbors are alive in the current generation:

- A live cell with two or three living neighbors survives to the next generation.
- A live cell with more than three or less than two living neighbors dies in the next generation.
- A dead cell with exactly three living neighbors comes to life in the next generation.

## The Code

The code provided is the skeleton of a pygame implementation of Conway's Game of Life. While an authentic implementation would take place on an infinite grid, this one is restricted to a 10x10 grid. Code is included to initialize a board, represented as a matrix of booleans, as well as to actually draw the board and handle some input. Your objective is to complete the code so that it is a working program.

The tasks that remain to be done are to handle mouse input so that the user can click on the board to toggle the state of individual cells, and to actually implement the rules of Conway's Game of Life so that the program updates the state of the board correctly after each generation. You are highly encouraged to define additional functions to assist with either of these tasks.

Note that for the Game to work as intended, the state of every cell must be updated simultaneously. To achieve this, the "next" matrix is defined with the intention that it be used to track the state of all the cells in the next generation, and then have its values copied over to the current board after every cell has been processed. This way, you can update every cell in sequence without having the order of processing affect the end result.
