
import sys
sys.setrecursionlimit(3000)
real_data = [entry for entry in open('data.txt').read()]
for data in real_data:
	if data == " ":
		real_data.remove(data)
input_data = [int(entry) for entry in real_data]
test_data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

count = []

parsed_data = [int(entry) for entry in test_data.split()]
#print(parsed_data)

def solve(data, count):
	num_children = data.pop(0)
	meta_data = data.pop(0)
	print("hello")
	for i in range(num_children):
		solve(data, count)
	for i in range(meta_data):
		count.append(data.pop(0))

	return count


#print(len(input_data))
counter = solve(parsed_data, count)
print(sum(counter))

