"""
--- Day 6: Probably a Fire Hazard ---
 Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid. Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration. Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs.  Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.  The lights all start turned off.
 To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order. For example: 
turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
 turn on 0,0 through 999,999 would turn on (or leave on) every light. toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off. turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights. After following the instructions, how many lights are lit?
"""

import time
start_time = time.time()

lights1 = set()
lights2 = dict()
instructions = open('../Input/day6.txt','r').read().split('\n')

def process_instruction1(instruction):
	parts = instruction.split()
	if parts[0] == 'toggle':
		x1,y1 = [int(i) for i in parts[1].split(',')]
		x2,y2 = [int(i) for i in parts[3].split(',')]
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				if (x,y) in lights1:
					lights1.remove((x,y))
				else:
					lights1.add((x,y))

	else:
		x1,y1 = [int(i) for i in parts[2].split(',')]
		x2,y2 = [int(i) for i in parts[4].split(',')]
		if parts[1] == 'on':
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					lights1.add((x,y))

		else:
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					if (x,y) in lights1:
						lights1.remove((x,y))


def process_instruction2(instruction):
	parts = instruction.split()
	if parts[0] == 'toggle':
		x1,y1 = [int(i) for i in parts[1].split(',')]
		x2,y2 = [int(i) for i in parts[3].split(',')]
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				if (x,y) in lights2:
					lights2[(x,y)] += 2
				else:
					lights2[(x,y)] = 2

	else:
		x1,y1 = [int(i) for i in parts[2].split(',')]
		x2,y2 = [int(i) for i in parts[4].split(',')]
		if parts[1] == 'on':
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					if (x,y) in lights2:
						lights2[(x,y)] += 1
					else:
						lights2[(x,y)] = 1

		else:
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					if (x,y) in lights2:
						if (x,y) in lights2:
							if lights2[(x,y)] == 1:
								del lights2[(x,y)]
							else:
								lights2[(x,y)] -= 1

for inst in instructions:
	process_instruction1(inst)

print "Part I"
print len(lights1)

i = 0
for inst in instructions:
	process_instruction2(inst)
	if (i % 20 == 0):
		print i
	i += 1

print "Part II"
print sum(lights2.values())

total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
