# Game-of-life
Conway's Game of Life in python.

## 1. Introduction
The Game of Life, is a zero-player game first conceived by John Horton Conway in 1970. The game is played in a 2d grid. Each gridpoint represents a live or dead cell. On each generation, the following rules are applied.
1. Any live cell with fewer than two live neighbours dies.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies.
4. Any dead cell with exactly three live neighbours becomes a live cell.

For more info, visit https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#References
## 2. Code
The game is implemented using an object oriented approach and the Python programming language. The code consists of 3 files.

- life_source.py : The bulk of the code, contains the Life class which implements the game.
- utils.py : Utilities like initial seed reshape function, periodic BC index managment, some initial seeds , etc.
- run.py : The runfile of the program. The parameters are self explainatory.

Note that, as of now, the simulation grid is using periodic boundary conditions.

All classes, methods and functions have been thouroughly documented in the form of docstrings.
## 3. Examples
Below are some examplary animations created by the code for various initial seeds.


https://github.com/user-attachments/assets/a215c736-6dd7-4bc7-9faa-f939fc41560c 

https://github.com/user-attachments/assets/455aed5c-d8d9-4c95-bf6f-f691cb57dc59

https://github.com/user-attachments/assets/9266cc5a-bbff-4e00-bff2-59b93b922528

https://github.com/user-attachments/assets/b513663a-0764-4519-b13e-b720a7f68ed8

