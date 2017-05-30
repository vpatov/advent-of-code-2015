"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
 Santa needs help figuring out which strings in his text file are naughty or nice. A nice string is one with all of the following properties: 
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
 It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou. It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd). It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements. For example: 
ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
 ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings. aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap. jchzalrnumimnmhp is naughty because it has no double letter. haegwjzuvuyypxyu is naughty because it contains the string xy. dvszwmarrgswjxmb is naughty because it contains only one vowel. How many strings are nice?
"""

import time
start_time = time.time()

strings = open('../Input/day5.txt').read().split('\n')
vowels = set(['a','e','i','o','u'])
forbidden = set(['ab','cd','pq','xy'])

# Part I
# cond 1: must contain at least three vowels 
# cond 2: must contain at least one letter that appears twice in a row
# cond 3: must not contan any of the forbidden strings

def is_nice1(string):
	count_vowel = 0
	for ch in string:
		if ch in vowels:
			count_vowel += 1
	if count_vowel < 3:
		return False
	cond2 = False
	for i in range(len(string) - 1):
		if (string[i] == string[i+1]):
			cond2 = True
			break
	if (not cond2):
		return False
	for substr in forbidden:
		if substr in string:
			return False
	return True


# Part II
# cond 1: It contains a pair of any two letters that appears at least twice 
# in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), 
# but not like aaa (aa, but it overlaps).
# cond2: It contains at least one letter which repeats with exactly one 
# letter between them, like xyx, abcdefeghi (efe), or even aaa.
def is_nice2(string):
	
	cond1 = False
	first_pair = string[0:2]
	pairs = [first_pair]
	for i in range(2,len(string)):
		pair = string[i-1:i+1]
		j = len(pairs) - 2
		while (j >= 0):
			if pairs[j] == pair:
				cond1 = True
				break
			j -= 1

		pairs.append(pair)
	if not cond1:
		return False


	cond2 = False
	for i in range(0,len(string) - 2):
		if (string[i] == string[i+2]):
			cond2 = True
			break
	return cond2

print "Part I"
print len(filter(is_nice1,strings))
print "Part II"
print len(filter(is_nice2,strings))


total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
