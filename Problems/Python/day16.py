"""
--- Day 16: Aunt Sue ---
 Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card.  However, there's a small problem: she signed it "From, Aunt Sue". You have 500 Aunts named "Sue". So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift.  You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine!  Just what you wanted.  Or needed, as the case may be. The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect: 
children, by human DNA age analysis.
cats.  It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish.  No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
 children, by human DNA age analysis. cats.  It doesn't differentiate individual breeds. Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas. goldfish.  No other kinds of fish. trees, all in one group. cars, presumably by exhaust or gasoline or something. perfumes, which is handy, since many of your Aunts Sue wear a few kinds. In fact, many of your Aunts Sue have many of these.  You put the wrapping from the gift into the MFCSAM.  It beeps inquisitively at you a few times and then prints out a message on ticker tape: children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
 You make a list of the things you can remember about each Aunt Sue.  Things missing from your list aren't zero - you simply don't remember the value. What is the number of the Sue that got you the gift?
"""

import time
start_time = time.time()

mfscam_out = \
"""children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split('\n')

clues = {el[:el.index(':')]:int(el[-1]) for el in mfscam_out}

data = open('../Input/day16.txt').read().split('\n')
aunts = []
for line in data:
	parts = line.split()
	# each line only as three fields - I didn't check all 500 but I'll keep the assumption for now
	# Sue 477: cars: 6, perfumes: 5, vizslas: 2
	field1,val1,field2,val2,field3,val3 = (
		parts[2][:-1], 
		int(parts[3][:-1]),
		parts[4][:-1], 
		int(parts[5][:-1]),
		parts[6][:-1], 
		int(parts[7])
	)
	aunts.append({field1:val1,field2:val2,field3:val3})

print 'Part I'
for i in range(0,len(aunts)):
	the_one = True
	for clue in clues:
		if clue in aunts[i]:
			if aunts[i][clue] != clues[clue]:
				the_one = False
				break
	if (the_one):
		print i + 1
		break

print 'Part II'
for i in range(0,len(aunts)):
	the_one = True
	for clue in clues:
		if clue in aunts[i]:
			if clue in ['cats','trees']:
				if aunts[i][clue] <= clues[clue]:
					the_one = False
					break
			elif clue in ['pomeranians','goldfish']:
				if aunts[i][clue] >= clues[clue]:
					the_one = False
					break
			elif aunts[i][clue] != clues[clue]:
				the_one = False
				break
	if (the_one):
		print i + 1
		break





total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
