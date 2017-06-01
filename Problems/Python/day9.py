"""
--- Day 9: All in a Single Night ---
 Every year, Santa manages to deliver all of his presents in a single night. This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations.  He can start and end at any two (different) locations he wants, but he must visit each location exactly once.  What is the shortest distance he can travel to achieve this? For example, given the following distances: London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
 The possible routes are therefore: Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
 The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example. What is the distance of the shortest route?
"""

import time
from itertools import permutations
from math import factorial
start_time = time.time()

data = open('../Input/day9.txt','r').read().split('\n')
routes = dict()

for line in data:
	parts = line.split()
	from_city = parts[0]
	to_city = parts[2]
	cost = int(parts[4])
	if from_city in routes:
		routes[from_city][to_city] = cost
	else:
		routes[from_city] = {to_city:cost}
	if to_city in routes:
		routes[to_city][from_city] = cost
	else:
		routes[to_city] = {from_city:cost}

perms = permutations(routes.keys())
min_cost = float('inf')
max_cost = 0
num_perms = factorial(len(routes.keys()))

def try_path(path):
	tot_cost = 0
	i = 0
	while i < len(path) - 1:
		cur_city = path[i]
		next_city = path[i+1]
		routes_from_cur = routes[cur_city]
		if next_city in routes_from_cur:
			tot_cost += routes_from_cur[next_city]
		else:
			return (False,0,i)
		i += 1
	return (True,tot_cost,'_')

i = 0
while (i < num_perms):
	path = perms.next()
	valid, cost, index = try_path(path)
	if valid:
		if cost < min_cost:
			min_cost = cost
		if cost > max_cost:
			max_cost = cost
		i += 1
		continue

	else:
		skip = factorial(len(routes.keys()) - index)
		for _ in range(0,skip):
			perms.next()
		i += skip

print "Part I"
print min_cost
print "Part II"
print max_cost

total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
