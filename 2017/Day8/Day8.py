
from collections import defaultdict
from operator import lt, gt, eq, ne, le, ge

registers = defaultdict(int)

operators = {
	'<': lt,
	'>': gt,
	'==': eq,
	'!=': ne,
	'<=':le,
	'>=':ge
}


def main():

	file = open("Day8.txt", "r")
	instructions = file.readlines()
	maximal = 0
	for line in instructions:
		register, operation, value, _, cond_register, cond_operation, cond = line.split()
		value = int(value)
		cond = int(cond)
		if operators[cond_operation](registers[cond_register], cond):
			if operation == 'inc':
				registers[register] += value
			else:
				registers[register] -= value
				
		if registers[register] > maximal:
			maximal = registers[register]
		
	print(max(registers.values()))
	print(maximal)


if __name__ == '__main__':
	main()