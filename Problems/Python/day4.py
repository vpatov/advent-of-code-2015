"""
--- Day 4: The Ideal Stocking Stuffer ---
 Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys. To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.  The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash. For example: 
If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
 If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so. If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
"""

import time
import md5
start_time = time.time()

input_ = "iwrupvqb"
i = 0
while(True):
	m = md5.new()
	m.update(input_ + str(i))
	hash = m.hexdigest()
	if hash[0:5] == '00000':
		print "Part I"
		print i
		break
	i += 1
	
i = 0
while(True):
	m = md5.new()
	m.update(input_ + str(i))
	hash = m.hexdigest()
	if hash[0:6] == '000000':
		print "Part II"
		print i
		break
	i += 1
	



total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
