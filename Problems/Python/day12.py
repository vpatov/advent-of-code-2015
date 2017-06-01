"""
--- Day 12: JSAbacusFramework.io ---
 Santa's Accounting-Elves need help balancing the books after a recent order.  Unfortunately, their accounting software uses a peculiar storage format.  That's where you come in. They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings.  Your first job is to simply find all of the numbers throughout the document and add them together. For example: 
[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
 [1,2,3] and {"a":2,"b":4} both have a sum of 6. [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3. {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0. [] and {} both have a sum of 0. You will not encounter any strings containing numbers. What is the sum of all numbers in the document?
"""

import time,json
start_time = time.time()

json_obj = open('../Input/day12.txt','r').read()
json_obj = json.loads(json_obj)

tot_sum1 = 0
def evaluate1(obj):
	global tot_sum1
	if type(obj) == list:
		for el in obj:
			evaluate1(el)
	elif type(obj) == dict:
		for key in obj:
			evaluate1(obj[key])
	else:
		try:
			tot_sum1 += int(obj)
		except:
			pass

tot_sum2 = 0
def evaluate2(obj):
	global tot_sum2
	if type(obj) == list:
		for el in obj:
			evaluate2(el)
	elif type(obj) == dict:
		if "red" not in obj.values():
			for key in obj:
				evaluate2(obj[key])
	else:
		try:
			tot_sum2 += int(obj)
		except:
			pass

print 'Part I'
evaluate1(json_obj)
print tot_sum1
print 'Part II'
evaluate2(json_obj)
print tot_sum2


total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
