"""
--- Day 21: RPG Simulator 20XX ---
 Little Henry Case got a new video game for Christmas.  It's an RPG, and he's stuck on a boss.  He needs to know what equipment to buy at the shop.  He hands you the controller. In this game, the player (you) and the enemy (the boss) take turns attacking.  The player always goes first.  Each attack reduces the opponent's hit points by at least 1.  The first character at or below 0 hit points loses. Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score.  An attacker always does at least 1 damage.  So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points.  If the defender had an armor score of 300, the defender would still lose 1 hit point. Your damage score and armor score both start at zero.  They can be increased by buying items in exchange for gold.  You start with no items and have as much gold as you need.  Your total damage or armor is equal to the sum of those stats from all of your items.  You have 100 hit points. Here is what the item shop is selling: Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
 You must buy exactly one weapon; no dual-wielding.  Armor is optional, but you can't use more than one.  You can buy 0-2 rings (at most one for each hand).  You must use any items you buy.  The shop only has one of each item, so you can't buy, for example, two rings of Damage +3. For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor: 
The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
 The player deals 5-2 = 3 damage; the boss goes down to 9 hit points. The boss deals 7-5 = 2 damage; the player goes down to 6 hit points. The player deals 5-2 = 3 damage; the boss goes down to 6 hit points. The boss deals 7-5 = 2 damage; the player goes down to 4 hit points. The player deals 5-2 = 3 damage; the boss goes down to 3 hit points. The boss deals 7-5 = 2 damage; the player goes down to 2 hit points. The player deals 5-2 = 3 damage; the boss goes down to 0 hit points. In this scenario, the player wins!  (Barely.) You have 100 hit points.  The boss's actual stats are in your puzzle input.  What is the least amount of gold you can spend and still win the fight?
"""

import time
start_time = time.time()

boss_stats = {"hp":100,"damage":8,"armor":2}
your_stats = {"hp":100,"damage":0,"armor":0}

weapons_shop = dict()
armor_shop = dict()
rings_shop = dict()
data = open('../Input/day21.txt','r').read().split('\n')
cur = None
for line in data:
	if len(line) < 1:
		continue
	parts = line.split()
	if parts[0][:-1] == 'Weapons':
		cur = weapons_shop
		continue
	elif parts[0][:-1] == 'Armor':
		cur = armor_shop
		continue
	elif parts[0][:-1] == 'Rings':
		cur = rings_shop
		continue
	name,cost,damage,armor = parts[0],int(parts[-3]),int(parts[-2]),int(parts[-1])
	if cur == rings_shop:
		name = parts[0] + ' ' + parts[1]

	cur[name] = {'cost':cost,'damage':damage,'armor':armor}

#Add two zero cost no effect rings to the shop to make the case of no rings easier to represent
armor_shop['zero_armor'] = {'cost':0,'damage':0,'armor':0}
rings_shop['zero_ring1'] = {'cost':0,'damage':0,'armor':0}
rings_shop['zero_ring2'] = {'cost':0,'damage':0,'armor':0}

# return True if you win
def fight(boss,you):
	boss_hp,your_hp = boss['hp'],you['hp']
	boss_dmg,your_dmg = boss['damage'],you['damage']
	boss_armr,your_armr = boss['armor'],you['armor']

	your_turn = True
	while (True):
		if your_turn:
			boss_hp -= max(1,your_dmg - boss_armr)
			if boss_hp <= 0:
				return True
		else:
			your_hp -= max(1,boss_dmg - your_armr)
			if your_hp <= 0:
				return False
		
		your_turn = not your_turn

print weapons_shop
print armor_shop
print rings_shop

min_cost = float('inf')
max_cost = 0
for weapon in weapons_shop.values():
	for armor in armor_shop.values():
		for ring1 in rings_shop:
			for ring2 in rings_shop:
				if ring1 == ring2:
					continue
				your_stats['damage'] = weapon['damage'] + rings_shop[ring1]['damage'] + rings_shop[ring2]['damage']
				your_stats['armor'] = armor['armor'] + rings_shop[ring1]['armor'] + rings_shop[ring2]['armor']
				cost = weapon['cost'] + armor['cost'] + rings_shop[ring1]['cost'] + rings_shop[ring2]['cost']

				win = fight(boss_stats,your_stats)
				if win:
					if cost < min_cost:
						min_cost = cost
				else:
					if cost > max_cost:
						max_cost = cost


print 'Part I'
print min_cost
print 'Part II'
print max_cost





total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
