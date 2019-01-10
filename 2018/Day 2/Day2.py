
from itertools import combinations, compress

def main():

	data = open("data.txt", "r")
	text_inputs = []
	twos = 0
	threes = 0
	for line in data:
		stripped_line = line.strip('\n')
		text_inputs.append(stripped_line)

	for entry in text_inputs:
		if two_count(entry) == True:
			twos += 1
		if three_count(entry) == True:
			threes += 1
	answer = twos * threes


def two_count(entry):
	 for letter in entry:
	 	count = entry.count(letter)
	 	if count == 2:
	 		return True
	 return False

def three_count(entry):
	for letter in entry:
		count = entry.count(letter)
		if count == 3:
			return True
	return False	

if __name__ == '__main__':
	main()
	blah()