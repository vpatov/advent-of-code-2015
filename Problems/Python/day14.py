"""
--- Day 14: Reindeer Olympics ---
 This year is the Reindeer Olympics!  Reindeer can fly at high speeds, but must rest occasionally to recover their energy.  Santa would like to know which of his reindeer is fastest, and so he has them race. Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state. For example, suppose you have the following Reindeer: 
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
 Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds. Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds. After one second, Comet has gone 14 km, while Dancer has gone 16 km.  After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.  On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km.  On the 12th second, both reindeer are resting.  They continue to rest until the 138th second, when Comet flies for another ten seconds.  On the 174th second, Dancer flies for another 11 seconds. In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point).  So, in this situation, Comet would win (if the race ended at 1000 seconds). Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
"""

import time
start_time = time.time()

fly_time = 2503
data = open('../Input/day14.txt','r').read().split('\n')
reindeers = dict()
for line in data:
	parts = line.split()
	name,speed,flight_time,rest_time = parts[0],int(parts[3]),int(parts[6]),int(parts[-2])
	reindeers[name] = {'speed':speed,'flight_time':flight_time,'rest_time':rest_time}

positions = {deer:0 for deer in reindeers}
rest_left = {deer:0 for deer in reindeers}
flight_left = {deer:stats['flight_time'] for deer,stats in reindeers.iteritems()}
points = {deer:0 for deer in reindeers}

while (fly_time > 0):
	for deer in reindeers:
		if (rest_left[deer]):
			rest_left[deer] -= 1
			if (not rest_left[deer]):
				flight_left[deer] = reindeers[deer]['flight_time']
			continue
		if (flight_left[deer]):
			positions[deer] += reindeers[deer]['speed']
			flight_left[deer] -= 1
			if (not flight_left[deer]):
				rest_left[deer] = reindeers[deer]['rest_time']
			continue
	# we must wait for all of them to move before we see who is in the lead
	for deer in reindeers:
		if (positions[deer] == max(positions.values())):
			points[deer] += 1
	fly_time -= 1

print 'Part I'
print max(positions.values())
print 'Part II'
print max(points.values())

total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
 