"""
--- Day 19: Medicine for Rudolph ---
 Rudolph the Red-Nosed Reindeer is sick!  His nose isn't shining very brightly, and he needs medicine. Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine.  Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either. The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need.  It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule. However, the machine has to be calibrated before it can be used.  Calibration involves determining the number of molecules that can be generated in one step from a given starting point. For example, imagine a simpler machine that supports only the following replacements: H => HO
H => OH
O => HH
 Given the replacements above and starting with HOH, the following molecules could be generated: 
HOOH (via H => HO on the first H).
HOHO (via H => HO on the second H).
OHOH (via H => OH on the first H).
HOOH (via H => OH on the second H).
HHHH (via O => HH).
 HOOH (via H => HO on the first H). HOHO (via H => HO on the second H). OHOH (via H => OH on the first H). HOOH (via H => OH on the second H). HHHH (via O => HH). So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O). The machine replaces without regard for the surrounding characters.  For example, given the string H2O, the transition H => OO would result in OO2O. Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine.  How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?
"""

import time, re
start_time = time.time()

data = open('../Input/day19.txt','r').read().split('\n')
replacements = dict()
for line in data[:-1]:
	if len(line) > 1:
		parts = line.split()
		to_,from_ = parts[0],parts[2]
		if to_ in replacements:
			replacements[to_].append(from_)
		else:
			replacements[to_] = [from_]

main_molecule = data[-1]

reverse_lookup = dict()
for key,val in replacements.iteritems():
	for item in val:
		reverse_lookup[item] = key


reverse_regs = {}
for key in reverse_lookup:
	reverse_regs[key] = re.compile(key)


def process_molecule(molecule):
	combos = set()
	i,count = 0,0
	while (i < len(molecule)):
		cur_rep = molecule[i]
		start = i
		if i < len(molecule) - 1 and molecule[i+1].islower():
			cur_rep += molecule[i+1]
			i += 2
		else:
			i += 1
		if cur_rep in replacements:
			for rep in replacements[cur_rep]:			
				combos.add(molecule[:start] + rep + molecule[start + len(cur_rep):])
	return combos


def reduce_molecule(molecule):
	combos = set()
	i,count = 0,0
	for string in reverse_regs:
		if reverse_lookup[string] == 'e' and len(molecule) > 3:
			continue
		pattern = reverse_regs[string]
		for m in pattern.finditer(molecule):
			cur_rep = m.group()
			start = m.start()
			rep = reverse_lookup[cur_rep]
			combos.add(molecule[:start] + rep + molecule[start + len(cur_rep):])
	return combos


def decompose_molecule(molecule,steps):
	if molecule == 'e':
		return steps
	combos = reduce_molecule(molecule)
	steps += 1
	for combo in combos:
		res = decompose_molecule(combo,steps)
		if (res):
			return res



print 'Part I'
combos = process_molecule(main_molecule)
print len(combos)
print 'Part II'
print decompose_molecule(main_molecule,0)



total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
