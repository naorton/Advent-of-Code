
data = open("data.txt").read()

data = [entry for entry in data]
print(data)

level = 0
count = -1
for entry in data:
	count += 1
	if entry == "(":
		level += 1
	if entry == ")":
		level -= 1
	if level == -1:
		print(count)
print(level)