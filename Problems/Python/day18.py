"""
--- Day 18: Like a GIF For Your Yard ---
 After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed.  You arrange them in a 100x100 grid. Never one to let you down, Santa again mails you instructions on the ideal lighting configuration.  With so few lights, he says, you'll have to resort to animation. Start by setting your lights to the included initial configuration (your puzzle input).  A # means "on", and a . means "off". Then, animate your grid in steps, where each step decides the next configuration based on the current one.  Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals).  Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off". For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5: 1B5...
234...
......
..123.
..8A4.
..765.
 The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on: 
A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
 A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise. A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise. All of the lights update simultaneously; they all consider the same current state before moving to the next. Here's a few steps from an example configuration of another 6x6 grid: Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
 After 4 steps, this example has four lights on. In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
"""

import time
start_time = time.time()

grid = []
data = open('../Input/day18.txt','r').read().split('\n')
for line in data:
	row = [1 if i == '#' else 0 for i in line]
	grid.append(row)

neighbors = lambda i,j: [(i-1,j),(i-1,j-1),(i-1,j+1),
				(i,j-1),(i,j+1), 
				(i+1,j),(i+1,j-1),(i+1,j+1) 
			]

def process_grid1(grid):
	new_grid = [[0 for i in range(len(grid))] for j in range(len(grid))]
	for i in range(0,len(grid)):
		for j in range(0,len(grid[i])):
			count_on = 0
			for x,y in neighbors(i,j):
				try:
					if x < 0 or y < 0:
						continue
					light = grid[x][y]
					if light == 1:
						count_on += 1
				except Exception as e:
					pass

			if grid[i][j]:
				if count_on in [2,3]:
					new_grid[i][j] = 1
			else:
				if count_on == 3:
					new_grid[i][j] = 1
	return new_grid

def process_grid2(grid):
	new_grid = [[0 for i in range(len(grid))] for j in range(len(grid))]
	for i in range(0,len(grid)):
		for j in range(0,len(grid[i])):
			count_on = 0
			for x,y in neighbors(i,j):
				try:
					if x < 0 or y < 0:
						continue
					light = grid[x][y]
					if light == 1:
						count_on += 1
				except Exception as e:
					pass

			if grid[i][j]:
				if count_on in [2,3]:
					new_grid[i][j] = 1
			else:
				if count_on == 3:
					new_grid[i][j] = 1
	new_grid[0][0] = 1
	new_grid[0][len(new_grid)-1] = 1
	new_grid[len(new_grid) - 1][0] = 1
	new_grid[len(new_grid) - 1][len(new_grid) - 1] = 1

	return new_grid


print 'Part I'
for _ in range(100):
	grid = process_grid1(grid)
print sum([sum(row) for row in grid])

# reset the grid
grid = []
data = open('../Input/day18.txt','r').read().split('\n')
for line in data:
	row = [1 if i == '#' else 0 for i in line]
	grid.append(row)

	
print 'Part II'
for _ in range(100):
	grid = process_grid2(grid)
print sum([sum(row) for row in grid])

total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
