"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
 Santa is delivering presents to an infinite two-dimensional grid of houses. He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next.  Moves are always exactly one house to the north (^), south (v), east (>), or west (<).  After each move, he delivers another present to the house at his new location. However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once.  How many houses receive at least one present? For example: 
> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
 > delivers presents to 2 houses: one at the starting location, and one to the east. ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location. ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

import time
start_time = time.time()

visited1 = set()
visited2 = set()
x,y,rx,ry,sx,sy = 0,0,0,0,0,0
robots_turn = False

contents = open('../Input/day3.txt').read()
visited1.add((x,y))
visited2.add((sx,sy))

# Yes, I know you can imitate a switch statement in Python using a dictionary, but I
# bothered not with that because this is not performance-critical code.
for ch in contents:
	if ch == '<':
		if robots_turn:
			rx -= 1
		else:
			sx -= 1
		x -= 1
	elif ch == '>':
		if robots_turn:
			rx += 1
		else:
			sx += 1
		x += 1
	elif ch == 'v':
		if robots_turn:
			ry -= 1
		else:
			sy -= 1
		y -= 1
	else:
		if robots_turn:
			ry += 1
		else:
			sy += 1
		y += 1

	cur1 = (x,y)
	cur2 = (rx,ry) if robots_turn else (sx,sy)

	visited1.add(cur1)
	visited2.add(cur2)
	robots_turn = not robots_turn
	

print "Part I"
print len(visited1)
print "Part II"
print len(visited2)
	
total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
