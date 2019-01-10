
def main(count, count_array):

	data = open("Data.txt", "r")
	for line in data:

		if '-' in line:

			subtract = line.split('-')
			subtract[1] = subtract[1].rstrip()
			
			count -= int(subtract[1])

		elif '+' in line:

			addition = line.split('+')
			addition[1] = addition[1].rstrip()
			
			count += int(addition[1])

		count_array.append(count)

	return count, count_array

def firstduplicate(count_array):
	repeat = set()
	for item in count_array:
		if item in repeat:
			return item
		repeat.add(item)
	return None

if __name__ == '__main__':
	count = 0
	count_array = []
	first_repeat = None
	while first_repeat == None:
		count, count_array = main(count, count_array)
		first_repeat = firstduplicate(count_array)

	print(first_repeat)
