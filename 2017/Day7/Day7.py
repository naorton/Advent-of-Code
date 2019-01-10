
def main():
	
	data = []
	tower = {}
	parents = {}
	node = []
	file = open("Day7.txt", "r")

	
	for line in file:
		
		name = line.split()
		data.append(name)
		
	#print(tower)

	for entry in data:
		
		if len(entry) == 2:
				
			tower[entry[0]] = [entry[1]]
		
		else:
			node.append(entry)
			
	for name in node:
	
		for i,entry in enumerate(name):
			name[i] = entry.replace(',', '')
	
	for entry in node:
		i = 3
		temp = []
		while i < len(entry):
			
			temp.append(entry[i])
			i += 1
		parents[entry[0]] = [[entry[1]], temp]
		
	#print(tower)
	top = next(iter(tower))
	print(top)
	for entry in parents:
		print('entry: ' + str(entry))
		if top in parents[entry][1]:
			top = entry
			
		for entry in parents:
			if top in parents[entry][1]:
				top = entry
	print(top)
			


	
		













if __name__ == '__main__':
	main()