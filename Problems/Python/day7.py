"""
--- Day 7: Some Assembly Required ---
 This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates!  Unfortunately, little Bobby is a little under the recommended age 
 range, and he needs help assembling the circuit. Each wire has an identifier (some lowercase letters) and can 
 carry a 16-bit signal (a number from 0 to 65535).  A signal is provided to each wire by a gate, another wire, 
 or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple 
 \destinations.  A gate provides no signal until all of its inputs have a signal. The included instructions booklet 
 describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then
  connect its output to wire z. For example: 
123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
 123 -> x means that the signal 123 is provided to wire x. x AND y -> z means that the 
 bitwise AND of wire x and wire y is provided to wire z. p LSHIFT 2 -> q means that the value
  from wire p is left-shifted by 2 and then provided to wire q. NOT e -> f means that the bitwise 
  complement of the value from wire e is provided to wire f. Other possible gates include OR (bitwise OR) and 
  RSHIFT (right-shift).  If, for some reason, you'd like to emulate the circuit instead, almost all programming 
  languages (for example, C, JavaScript, or Python) provide operators for these gates. For example, here is a simple
   circuit: 
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
 After it is run, these are the signals on the wires: d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
 In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
"""

import time
start_time = time.time()

# get the problem input
instructions1 = open('../Input/day7.txt','r').read().split('\n')
instructions2 = open('../Input/day7_part2.txt','r').read().split('\n') # I manually put in the answer from part 1 into the file of part 2

# use dontcares so that each instruction can have the same format - elegance!
operations = {
	'AND':lambda x,y: x & y,
	'OR' :lambda x,y: x | y,
	'LSHIFT': lambda x,y: x << y,
	'RSHIFT': lambda x,y: x >> y,
	'NOT': lambda x,_: ~x,
	'SELF':lambda x,_: x
	}

wires = dict()

def process_instruction(instruction):
	parts = instruction.split()
	end_wire = parts[-1]
	if 'NOT' in parts:
		try:
			val = int(parts[1])
			wires[end_wire] = ~val
		except:
			wires[end_wire] = ('NOT',parts[1],"IGNORE")
	elif len(parts) == 3:
		wires[end_wire] = ('SELF',parts[0],"IGNORE")
	else: #handles AND, OR, LSHIFT, RSHIFT
		wires[end_wire] = (parts[1],parts[0],parts[2])

def evaluate(wire):
	if wire == "IGNORE": return None
	if wire in wires:
		try:
			return int(wires[wire])
		except:
			operation,op1,op2 = wires[wire]
			if operation == 'SELF':
				try:
					wires[wire] = int(op1)
					return wires[wire]
				except:
					pass
			wires[wire] = operations[operation](evaluate(op1),evaluate(op2))
			return wires[wire]
	else: return int(wire)


print "Part I"	
for inst in instructions1:
	process_instruction(inst)

print evaluate('a')

wires = dict() #reset the wires
print "Part II"	
for inst in instructions2:
	process_instruction(inst)

print evaluate('a')
total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
