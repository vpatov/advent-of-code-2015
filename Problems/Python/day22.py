"""
--- Day 22: Wizard Simulator 20XX ---
 Little Henry Case decides that defeating bosses with swords and stuff is boring.  Now he's playing the game with a wizard.  Of course, he gets stuck on another boss and needs your help again. In this version, combat still proceeds with the player and the boss taking alternating turns.  The player still goes first.  Now, however, you don't get any equipment; instead, you must choose one of your spells to cast.  The first character at or below 0 hit points loses. Since you're a wizard, you don't get to wear armor, and you can't attack normally.  However, since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well.  As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage. On each of your turns, you must select one of your spells to cast.  If you cannot afford to cast any spell, you lose.  Spells cost mana; you start with 500 mana, but have no maximum limit.  You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it.  Your spells are Magic Missile, Drain, Shield, Poison, and Recharge. 
Magic Missile costs 53 mana.  It instantly does 4 damage.
Drain costs 73 mana.  It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana.  It starts an effect that lasts for 6 turns.  While it is active, your armor is increased by 7.
Poison costs 173 mana.  It starts an effect that lasts for 6 turns.  At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana.  It starts an effect that lasts for 5 turns.  At the start of each turn while it is active, it gives you 101 new mana.
 Magic Missile costs 53 mana.  It instantly does 4 damage. Drain costs 73 mana.  It instantly does 2 damage and heals you for 2 hit points. Shield costs 113 mana.  It starts an effect that lasts for 6 turns.  While it is active, your armor is increased by 7. Poison costs 173 mana.  It starts an effect that lasts for 6 turns.  At the start of each turn while it is active, it deals the boss 3 damage. Recharge costs 229 mana.  It starts an effect that lasts for 5 turns.  At the start of each turn while it is active, it gives you 101 new mana. Effects all work the same way.  Effects apply at the start of both the player's turns and the boss' turns.  Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one.  If this decreases the timer to zero, the effect ends.  You cannot cast a spell that would start an effect which is already active.  However, effects can be started on the same turn they end. For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage: -- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
 Now, suppose the same initial conditions, except that the boss has 14 hit points instead: -- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
 You start with 50 hit points and 500 mana points. The boss's actual stats are in your puzzle input. What is the least amount of mana you can spend and still win the fight?  (Do not include mana recharge effects as "spending" negative mana.)
"""

import time
import itertools
start_time = time.time()

boss_stats = {'hp':58,'damage':9}
your_stats = {'hp':50,'mana':500}
spell_costs = {'Magic Missile':53,'Drain':73,'Shield':113,'Poison':173,'Recharge':229}
minimum_mana = 53

def fight(boss_stats,your_stats,spell_seq,part2):
	boss_hp,your_hp = boss_stats['hp'],your_stats['hp']
	boss_dmg = boss_stats['damage']
	your_mana = your_stats['mana']
	your_armor = 0
	mana_spent = 0

	current_spell = 0
	poison_ticker = 0
	shield_ticker = 0
	recharge_ticker = 0
	your_turn = True
	while(True):

		if poison_ticker:
			boss_hp -= 3
			poison_ticker -= 1
		if boss_hp <= 0:
			return True,mana_spent

		#shield
		if shield_ticker:
			shield_ticker -= 1
			if shield_ticker == 0:
				your_armor = 0

		#recharge
		if recharge_ticker:
			recharge_ticker -= 1
			your_mana += 101

		if your_turn:
			if part2:
				your_hp -= 1
				if your_hp <= 0:
					return False


			if your_mana < minimum_mana:
				return False
			if current_spell == len(spell_seq):
				return False

			spell = spell_seq[current_spell]
			current_spell += 1
			your_mana -= spell_costs[spell]
			mana_spent += spell_costs[spell]
			if spell == 'Magic Missile':
				boss_hp -= 4

			elif spell == 'Drain':
				boss_hp -= 2
				your_hp += 2

			elif spell == 'Shield':
				shield_ticker = 6
				your_armor = 7

			elif spell == 'Recharge':
				recharge_ticker = 5

			elif spell == 'Poison':
				poison_ticker = 6

			if boss_hp <= 0:
				return True,mana_spent
		else:
			your_hp -= max(1,boss_dmg - your_armor)
			if your_hp <= 0:
				return False
		
		your_turn = not your_turn

valid_seqs = []
length_seq = 9 # I tried different values for length_seq. This is the lowest one that returned the right answer
seqs = itertools.product(spell_costs,repeat=length_seq)
i = 0

while(i < len(spell_costs) ** length_seq):
	seq = seqs.next()
	skip = 0
	for j in range(len(seq)):
		if seq[j] == 'Poison':
			if 'Poison' in seq[j+1:j+3]:
				ind = seq[j+1:j+3].index('Poison') + j + 1
				skip = len(spell_costs) ** (length_seq - ind - 1)
				break
		elif seq[j] == 'Shield':
			if 'Shield' in seq[j+1:j+3]:
				ind = seq[j+1:j+3].index('Shield') + j + 1
				skip = len(spell_costs) ** (length_seq - ind - 1)
				break
		elif seq[j] == 'Recharge':
			if 'Recharge' in seq[j+1:j+3]:
				ind = seq[j+1:j+3].index('Recharge') + j + 1
				skip = len(spell_costs) ** (length_seq - ind - 1)
				break
	if skip:
		i += skip
		# start skip > 1 to not double count the current seq
		while (skip > 1):
			seqs.next()
			skip -= 1
	else:
		valid_seqs.append(seq)
		i+=1
print 'number of valid sequences:' len(valid_seqs)
min_mana_spent1 = float('inf')
min_mana_spent2 = float('inf')
for seq in valid_seqs:
	res1 = fight(boss_stats,your_stats,seq,part2=False)
	if (res1):
		mana_spent = res1[1]
		if mana_spent < min_mana_spent1:
			min_mana_spent1 = mana_spent

	res2 = fight(boss_stats,your_stats,seq,part2=True)
	if (res2):
		mana_spent = res2[1]
		if mana_spent < min_mana_spent2:
			min_mana_spent2 = mana_spent

print 'Part I'
print min_mana_spent1
print 'Part II'
print min_mana_spent2


total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
