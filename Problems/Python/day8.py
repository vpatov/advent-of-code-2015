"""
--- Day 8: Matchsticks ---
 Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. 
 He needs to know how much space it will take up when stored. It is common in many programming languages
  to provide a way to escape special characters in strings.  For example, C, JavaScript, Perl, Python, 
  and even PHP handle special characters in very similar ways. However, it is important to realize the
   difference between the number of characters in the code representation of the string literal and the
    number of characters in the in-memory string itself. For example: 
"" is 2 characters of code (the two double quotes), but the string contains zero characters.
"abc" is 5 characters of code, but 3 characters in the string data.
"aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a 
single, escaped quote character, for a total of 7 characters in the string data.
 is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using 
 hexadecimal notation.
 "" is 2 characters of code (the two double quotes), but the string contains zero characters. "abc" is 
 5 characters of code, but 3 characters in the string data. "aaa\"aaa" is 10 characters of code, but the
  string itself contains six "a" characters and a single, escaped quote character, for a total of 7 
  characters in the string data. "/x27" is 6 characters of code, but the string itself contains just 
  one - an apostrophe ('), escaped using hexadecimal notation. Santa's list is a file that 
  contains many double-quoted string literals, one on each line.  The only escape sequences 
  used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), 
  and  plus two hexadecimal characters (which represents a single character with that ASCII code). 
  Disregarding the whitespace in the file, what is the number of characters of code for string 
  literals minus the number of characters in memory for the values of the strings in total for
   the entire file? For example, given the four strings above, the total number of characters of 
   string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string 
   values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
"""

import time
import re
hex_num = re.compile(r'[0-9abcdef]{2}')
start_time = time.time()

strings = open('../Input/day8.txt','r').read().split('\n')


def count_mem(string):
	count = 0
	escaped = False
	i = 1
	while (i < len(string)-1):
		if (string[i] == '\\' and not escaped):
			escaped = True
			i += 1
			continue
		elif (string[i] == '\\' and escaped):
			count += 1
			escaped = False
			i += 1
			continue
		elif (string[i] == 'x' and escaped):
			assert(hex_num.match(string[i+1:i+3]))
			count += 1
			escaped = False
			i += 3
			continue
		elif (string[i] == '"' and escaped):
			count += 1
			escaped = False
			i += 1
			continue
		else:
			count += 1
			i += 1
	return count

def encode(string):
	new_str = ['"']
	needs_escape = ['"','\\']
	i = 0
	while (i < len(string)):
		if string[i] in needs_escape:
			new_str.append('\\')
			new_str.append(string[i])
			i += 1
			continue
		else:
			new_str.append(string[i])
			i += 1
	new_str.append('"')
	return len(new_str)

tot_char_length = 0
tot_count_mem = 0
tot_encode_length = 0
for string in strings:
	tot_char_length += len(string)
	tot_count_mem += count_mem(string)
	tot_encode_length += encode(string)

print "Part I"
print tot_char_length - tot_count_mem
print "Part II"
print tot_encode_length - tot_char_length

print(encode('"abc"'))





total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
