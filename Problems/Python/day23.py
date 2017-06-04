"""
--- Day 23: Opening the Turing Lock ---
 Little Jane Marie just got her very first computer for Christmas from some unknown benefactor.  It comes with instructions and an example program, but the computer itself seems to be malfunctioning.  She's curious what the program does, and would like you to help her run it. The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0.  The instructions are as follows: 
hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
 hlf r sets register r to half its current value, then continues with the next instruction. tpl r sets register r to triple its current value, then continues with the next instruction. inc r increments register r, adding 1 to it, then continues with the next instruction. jmp offset is a jump; it continues with the instruction offset away relative to itself. jie r, offset is like jmp, but only jumps if register r is even ("jump if even"). jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd). All three jump instructions work with an offset relative to that instruction.  The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively).  For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever. The program exits when it tries to run an instruction beyond the ones defined. For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction: inc a
jio a, +2
tpl a
inc a
 What is the value in register b when the program in your puzzle input is finished executing?
"""

import time
start_time = time.time()

code = open('../Input/day23.txt','r').read().split('\n')


pc = 0
registers = {'a':0,'b':0}
instructions = {
	'hlf':lambda r,_: registers[r]/2,
	'tpl':lambda r,_: 3*registers[r],
	'inc':lambda r,_: registers[r] + 1,
	'jmp':lambda _,a: pc + a-1,
	'jie':lambda r,a: pc + a-1 if (registers[r] % 2 == 0) else pc,
	'jio':lambda r,a: pc + a-1 if (registers[r] == 1) else pc
}

def process_instruction(instruction):
	global pc
	inst = instruction.split()
	opcode = inst[0]
	a,r = 1,'a'
	if len(inst) == 3:
		r = inst[1][:-1]
		a = inst[2]
	elif opcode == 'jmp':
		a = inst[1]
	else:
		r = inst[1]

	if opcode in ['jmp','jie','jio']:
		pc = instructions[opcode](r,int(a))
	else:
		registers[r] = instructions[opcode](r,int(a))

	pc += 1

print 'Part I'
while(pc < len(code)):
	process_instruction(code[pc])
print registers['b']

print 'Part II'
pc = 0
registers = {'a':1,'b':0}
while(pc < len(code)):
	process_instruction(code[pc])
print registers['b']






total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
