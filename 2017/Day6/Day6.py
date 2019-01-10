

def main():
	
	file = open("Day6.txt", "r")
	states = [0]
	max_blocks = []
	count = 0


	file = file.read()
	memory = file.split()

	memory = list(map(int, memory))
	print(memory)
	
	
	state = ''.join(map(str,memory))
	#print(state)
	states.append(int(state))
	#print(states)
	#print(len(states))
	#print(len(set(states)))
	
	while len(states) == len(set(states)):
		#print(states)
		max_block = max(memory)
		#print("max: " + str(max_block))
		for i, memory_bank in enumerate(memory):
			if memory_bank == max_block:
				max_blocks.append(i)
	
		index = min(max_blocks)
		#print('index: ' + str(index))
		temp = memory[index]
		#print('temp: ' + str(temp))
		memory[index] = 0
		#print('memory length: ' + str(len(memory)))
		
		while temp > 0:
				if index >= len(memory) - 1:
					index = -1
				memory[index + 1] = memory[index + 1] + 1
				#print('value: ' + str(memory[index + 1]))
				index = index + 1
				#print('index: ' + str(index))
				temp = temp - 1
				#print('temp: ' + str(temp))
				
		count = count + 1
		state = ''.join(map(str,memory))
		states.append(int(state))
		max_blocks.clear()
		#print(memory)
		#print(states)
		#print(len(states))
		#print(len(set(states)))
		
	print('count: ' + str(count))
	
	for i, x in enumerate(states):
		if x == int(state):
			print(i)
		
	
if __name__ == '__main__':
	main()