
'''
old_keypad = {
	(0, 0): "7",
	(1, 0): "8",
	(2, 0): "9",
	(0, 1): "4",
	(1, 1): "5",
	(2, 1): "6",
	(0, 2): "1",
	(1, 2): "2",
	(2, 2): "3"
}
'''
new_keypad = {
	(0, 2):   "1",
	(-1, 1):  "2",
	(0, 1):   "3",
	(1, 1):   "4",
	(-2, 0):  "5",
	(-1, 0):  "6",
	(0, 0):   "7",
	(1, 0):   "8",
	(2, 0):   "9",
	(-1, -1): "A",
	(0, -1):  "B",
	(1, -1):  "C",
	(0, -2):  "D"
}

data = [entry for entry in open("data.txt").readlines()]
#data = ["ULL", "RRDDD", "LURDL", "UUUUD"]

def up(x, y):
	if x == -2 and y == 0:
		return x, y
	elif x == -1 and y == 1:
		return x, y
	elif x == 0 and y == 2:
		return x, y
	elif x == 1 and y == 1:
		return x, y
	elif x == 2 and y == 0:
		return x, y
	else:
		y += 1
		return x, y

def down(x, y):
	if x == -2 and y == 0:
		return x, y
	elif x == -1 and y == -1:
		return x, y
	elif x == 0 and y == -2:
		return x, y
	elif x == 1 and y == -1:
		return x, y
	elif x == 2 and y == 0:
		return x, y
	else:
		y -= 1
		return x, y

def right(x, y):
	if x == 2 and y == 0:
		return x, y
	elif x == 1 and y == -1:
		return x, y
	elif x == 1 and y == 1:
		return x, y
	elif x == 0 and y == 2:
		return x, y
	elif x == 0 and y == -2:
		return x, y
	else:
		x += 1
		return x, y

def left(x, y):
	if x == -2 and y == 0:
		return x, y
	elif x == -1 and y == -1:
		return x, y
	elif x == -1 and y == 1:
		return x, y
	elif x == 0 and y == 2:
		return x, y
	elif x == 0 and y == -2:
		return x, y
	else:
		x -= 1
		return x, y

x = -2
y = 0
answer = []
for entry in data:
	for letter in entry:
		if letter == "\n":
			continue
		elif letter == "U":
			x, y = up(x, y)
		elif letter == "D":
			x, y = down(x, y)
		elif letter == "L":
			x, y = left(x, y)
		else:
			x, y = right(x, y)
	answer.append(new_keypad[(x, y)])
print(answer)