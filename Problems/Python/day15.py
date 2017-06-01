"""
--- Day 15: Science for Hungry People ---
 Today, you set out on the task of perfecting your milk-dunking cookie recipe.  All you have to do is find the right balance of ingredients. Your recipe leaves room for exactly 100 teaspoons of ingredients.  You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon: 
capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
 capacity (how well it helps the cookie absorb milk) durability (how well it keeps the cookie intact when full of milk) flavor (how tasty it makes the cookie) texture (how it improves the feel of the cookie) calories (how many calories it adds to the cookie) You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future.  The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories. For instance, suppose you have these two ingredients: Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
 Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties: 
A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
 A capacity of 44*-1 + 56*2 = 68 A durability of 44*-2 + 56*3 = 80 A flavor of 44*6 + 56*-2 = 152 A texture of 44*3 + 56*-1 = 76 Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of  62842880, which happens to be the best score possible given these ingredients.  If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero. Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
"""

import time
start_time = time.time()

# this is a constraint optimization problem. it is not linear due to its multiplicative aspect, and thus
# is made more complex by this. However, thankfully the solution space is fairly small (171700), and we 
# can just brute force this.

data = open('../Input/day15.txt').read().split('\n')
ingredients = dict()
#Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
for line in data:
	parts = line.split()
	# the [:-1] gets rid of the comma
	name,capacity,durability,flavor,texture,calories = (
		parts[0][:-1].lower(),
		int(parts[2][:-1]),
		int(parts[4][:-1]),
		int(parts[6][:-1]),
		int(parts[8][:-1]),
		int(parts[10])
	)

	ingredients[name] = {
		'capacity':capacity,
		'durability':durability,
		'flavor':flavor,
		'texture':texture,
		'calories':calories
	}

def cookie_score1(sugar,sprinkles,candy,chocolate):

	qualities = {'capacity':0,'durability':0,'flavor':0,'texture':0}
	amounts = {'sugar':sugar,'sprinkles':sprinkles,'candy':candy,'chocolate':chocolate}
	for quality in qualities:
		for ingredient in ingredients:
			qualities[quality] += ingredients[ingredient][quality]*amounts[ingredient]
		if qualities[quality] < 0:
				return 0

	score = 1
	for value in qualities.values():
		score *= value
	return score

def cookie_score2(sugar,sprinkles,candy,chocolate):

	qualities = {'capacity':0,'durability':0,'flavor':0,'texture':0,'calories':0}
	amounts = {'sugar':sugar,'sprinkles':sprinkles,'candy':candy,'chocolate':chocolate}
	for quality in qualities:
		for ingredient in ingredients:
			qualities[quality] += ingredients[ingredient][quality]*amounts[ingredient]
		if qualities[quality] < 0:
				return 0

	if (qualities['calories'] != 500):
		return 0
	score = 1
	for key in qualities:
		if key != 'calories':
			score *= qualities[key]
	return score


print 'Part I'
best_score1 = 0
i = 100
while (i >= 0):
	j = 100 - i
	while (j >= 0):
		k = 100 - i - j
		while(k >= 0):
			l = 100 - i - j - k
			while (l >= 0):
				score1 = cookie_score1(i,j,k,l)
				if score1 > best_score1:
					best_score1 = score1

				l -= 1
			k -= 1
		j -= 1
	i -= 1
print best_score1

print 'Part II'
best_score2 = 0
i = 100
while (i >= 0):
	j = 100 - i
	while (j >= 0):
		k = 100 - i - j
		while(k >= 0):
			l = 100 - i - j - k
			while (l >= 0):
				score2 = cookie_score2(i,j,k,l)
				if score2 > best_score2:
					best_score2 = score2
				
				l -= 1
			k -= 1
		j -= 1
	i -= 1
print best_score2

total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
