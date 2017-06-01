"""
--- Day 11: Corporate Policy ---
 Santa's previous password expired, and he needs help choosing a new one. To help him remember his new 
 password after the old one expires, Santa has devised a method of coming up with a password based on 
 the previous one.  Corporate policy dictates that passwords must be exactly eight lowercase letters 
 (for security reasons), so he finds his new password by incrementing his old password string
  repeatedly until it is valid. Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, 
  and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat
   with the next letter to the left until one doesn't wrap around. Unfortunately for Santa, a new 
   Security-Elf recently started, and he has imposed some additional password requirements: 
Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and 
so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other 
characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
 Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, 
 and so on, up to xyz. They cannot skip letters; abd doesn't count. Passwords may not contain the
  letters i, o, or l, as these letters can be mistaken for other characters and are therefore
   confusing. Passwords must contain at least two different, non-overlapping pairs of letters, 
   like aa, bb, or zz. For example: 
hijklmmn meets the first requirement (because it contains the straight hij) but fails the second
 requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
 hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l). abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement. abbcegjk fails the third requirement, because it only has one double letter (bb). The next password after abcdefgh is abcdffaa. The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed. Given Santa's current password (your puzzle input), what should his next password be?

-Passwords must include one increasing straight of at least three letters, 
 like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
-Passwords may not contain the letters i, o, or l, as these letters can be
 mistaken for other characters and are therefore confusing.
-Passwords must contain at least two different, non-overlapping 
pairs of letters, like aa, bb, or zz.
"""

import time
start_time = time.time()
input_ = 'hepxcrrq'

def increment(passwd):
	new_str = []
	i = len(passwd) - 1
	while(i >= 0):
		new_ch = chr((((ord(passwd[i]) - ord('a')) + 1) % 26 ) + ord('a'))
		new_str.insert(0,new_ch)
		if new_ch == 'a':
			i -=1
		else:
			break
	new_str = passwd[:i] + ''.join(new_str)
	return new_str


def is_valid(passwd):
	for ch in passwd:
		if ch in ['i','o','u']:
			return False
	cond2 = False
	for i in range(0,len(passwd) - 2):
		if ord(passwd[i]) == ord(passwd[i+1]) - 1 and ord(passwd[i+2]) - 2 == ord(passwd[i]):
			cond2 = True
			break
	if not cond2: return False
	first_pair = None
	i = 0
	while i < len(passwd) - 1:
		if passwd[i] == passwd[i+1]:
			if first_pair == None:
				first_pair = passwd[i]
			else:
				if passwd[i] != first_pair:
					return True
		i += 1
	return False

print 'Part I'
while(True):
	input_ = increment(input_)
	if is_valid(input_):
		print input_
		break
print 'Part II'
while(True):
	input_ = increment(input_)
	if is_valid(input_):
		print input_
		break






total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
