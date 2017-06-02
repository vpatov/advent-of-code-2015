"""
--- Day 20: Infinite Elves and Infinite Houses ---
 To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door.  He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on. Each Elf is assigned a number, too, and delivers presents to houses based on that number: 
The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....
 The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, .... The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, .... Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, .... There are infinitely many Elves, numbered starting with 1.  Each Elf delivers presents equal to ten times his or her number at each house. So, the first nine houses on the street end up like this: House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.
 The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents.  The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents. What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?
"""

import time
from math import sqrt
import itertools
start_time = time.time()

import math


# obtaining factors efficiently - taken from https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def get_factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

input_ = 34000000

print 'Part I'
i = 1000
while (True):
	factors = get_factors(i)
	num_presents = sum(factor*10 for factor in factors)
	if num_presents >= input_:
		part1_presents = num_presents
		print i
		break
	i += 1

print 'Part II'
houses = [0] * 50000000
for i in range(1,1000000):
	for j in range(1,51):
		houses[i*j] += i*11

for i in range(0,len(houses)):
	if houses[i] >= 34137600:
		print i
		break






total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
