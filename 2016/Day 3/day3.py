
#data = [[int(value) for value in entry.split()] for entry in open("data.txt").readlines()]
data = []


for entry in open("data.txt").readlines():
	temp = []
	for value in entry.split():
		temp.append(int(value))
	data += temp
'''
data = [
	101, 301, 501,
	102, 302, 502,
	103, 303, 503,
	201, 401, 601,
	202, 402, 602,
	203, 403, 603 
]
'''
new_data = []
i = 0
len_check = 0
three_check = 0
while len_check < len(data)-1:
	print(i)
	temp = [data[i], data[i+3], data[i+6]]
	temp.sort()
	new_data.append(temp)
	len_check = i+6
	i += 1
	three_check += 1
	if three_check == 3:
		i += 6
		three_check = 0

print(new_data)

count = 0
for entry in new_data:
	if entry[0] + entry[1] > entry[2]:
		count += 1
print(count)
