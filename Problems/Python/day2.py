"""
--- Day 2: I Was Told There Would Be No Math ---
 The elves are running low on wrapping paper, and so they need to submit an order for more.  They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need. Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.  The elves also need a little extra paper for each present: the area of the smallest side. For example: 
A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
 A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet. A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet. All numbers in the elves' list are in feet.  How many total square feet of wrapping paper should they order?
"""

import time
start_time = time.time()

f = open('../Input/day2.txt')
tot_sum = 0
ribbon = 0
for line in f:
	parts = line.strip().split('x')
	l,w,h = int(parts[0]),int(parts[1]),int(parts[2])
	product = (2 * l*w) + (2 * w*h) + (2 * h*l)
	
	# Part I
	tot_sum += product
	min_num = min(l*w, w*h, h*l)
	tot_sum += min_num
	
	#Part II
	
	max_num = max(l,w,h)
	if max_num == l:
		ribbon += w + w + h + h
	elif max_num == w:
		ribbon += l + l + h + h
	else:
		ribbon += l + l + w + w
		
	ribbon += l * w * h
	
print 'Part I', tot_sum
print 'Part II', ribbon

f.close()


total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
