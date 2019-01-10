from collections import defaultdict
data = [entry.split() for entry in open("data.txt").readlines()]
commands = []

#turn off 199,133 through 461,193
#toggle 322,558 through 977,958

for string in data:
	temp = []
	if len(string) == 4:
		temp.append(string[0])
		x, y = string[1].split(",")
		temp.append(int(x))
		temp.append(int(y))
		x, y = string[3].split(",")
		temp.append(int(x))
		temp.append(int(y))
	else:
		temp.append(string[1])
		x, y = string[2].split(",")
		temp.append(int(x))
		temp.append(int(y))
		x, y = string[4].split(",")
		temp.append(int(x))
		temp.append(int(y))
	commands.append(temp)

lights = defaultdict(int)

def range1(start, end):
	return range(start, end+1)

for i in range(1000):
	for j in range(1000):
		lights[(i, j)] = 0

for entry in commands:

	if entry[0] == "on":
		for i in range1(entry[1], entry[3]):
			for j in range1(entry[2], entry[4]):
				lights[(i, j)] += 1
	elif entry[0] == "off":
		for i in range1(entry[1], entry[3]):
			for j in range1(entry[2], entry[4]):
				if lights[(i, j)] == 0:
					continue
				else:
					lights[(i, j)] -= 1
	elif entry[0] == "toggle":
		for i in range1(entry[1], entry[3]):
			for j in range1(entry[2], entry[4]):
				lights[(i, j)] += 2
				#if lights[(i, j)] == 1:
				#	lights[(i, j)] = 0
				#else:
				#	lights[(i, j)] = 1
count = 0

for entry in lights.values():
	count += entry

print(count)
'''
#turn off 660,55 through 986,197
count = 0
for i in range1(499,500):
	for j in range1(499, 500):
		#print(i,j)
		count += 1
'''

