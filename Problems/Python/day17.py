"""
--- Day 17: No Such Thing as Too Much ---
 The elves bought too much eggnog again - 150 liters this time.  To fit it all into your refrigerator, you'll need to move it into smaller containers.  You take an inventory of the capacities of the available containers. For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters.  If you need to store 25 liters, there are four ways to do it: 
15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
 15 and 10 20 and 5 (the first 5) 20 and 5 (the second 5) 15, 5, and 5 Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
"""

import time
start_time = time.time()

liters = 150
containers = sorted([int(i) for i in open('../Input/day17.txt','r').read().split('\n')])


all_combos = []
count_combos = 0
def try_combo(index,total,combo):
	global count_combos,all_combos
	total += containers[index]
	combo.append(containers[index])
	if total == liters:
		all_combos.append(combo)
		return True
	if total > liters:
		return False
	else:
		for i in range(index+1,len(containers)):
			if try_combo(i,total,list(combo)):
				count_combos += 1

for i in range(0,len(containers)):
	try_combo(i,0,[])
print 'Part I'
print count_combos

print 'Part II'
print len(filter(lambda x: len(x) == min([len(combo) for combo in all_combos]),all_combos))
# I wrote this one-liner and it worked and gave the right answer on the first try. I can't believe it!

total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
