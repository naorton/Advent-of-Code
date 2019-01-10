import sys

def parse(file):
	directions = []
	data = open(file).readlines()
	data = data[0].split()
	for entry in data:
		entry = entry.strip()
		entry = entry.strip(",")
		directions.append(entry)
	return directions


def directionChanger(facing_direction, move_direction):
	if facing_direction == "North":
		facing_direction = northChanger(move_direction)
	elif facing_direction == "East":
		facing_direction = eastChanger(move_direction)
	elif facing_direction == "South":
		facing_direction = southChanger(move_direction)
	else:
		facing_direction = westChanger(move_direction)
	return facing_direction

def northChanger(move_direction):
	if move_direction == "R":
		return "East"
	else:
		return "West"

def eastChanger(move_direction):
	if move_direction == "R":
		return "South"
	else:
		return "North"

def southChanger(move_direction):
	if move_direction == "R":
		return "West"
	else:
		return "East"

def westChanger(move_direction):
	if move_direction == "R":
		return "North"
	else:
		return "South"

def northMover(steps, end_coordinates):
	for i in range(int(steps)):
		end_coordinates[1] += 1
		location = (end_coordinates[0], end_coordinates[1])
		if location in memory:
			print("distance:" + str(abs(end_coordinates[0]) + abs(end_coordinates[1])))
			sys.exit(0)
		memory.add(location)
	return end_coordinates

def eastMover(steps, end_coordinates):
	for i in range(int(steps)):
		end_coordinates[0] += 1
		location = (end_coordinates[0], end_coordinates[1])
		if location in memory:
			print("distance:" + str(abs(end_coordinates[0]) + abs(end_coordinates[1])))
			sys.exit(0)
		memory.add(location)
	return end_coordinates

def southMover(steps, end_coordinates):
	for i in range(int(steps)):
		end_coordinates[1] -= 1
		location = (end_coordinates[0], end_coordinates[1])
		if location in memory:
			print("distance:" + str(abs(end_coordinates[0]) + abs(end_coordinates[1])))
			sys.exit(0)
		memory.add(location)
	return end_coordinates


def westMover(steps, end_coordinates):
	for i in range(int(steps)):
		end_coordinates[0] -= 1
		location = (end_coordinates[0], end_coordinates[1])
		if location in memory:
			print("distance:" + str(abs(end_coordinates[0]) + abs(end_coordinates[1])))
			sys.exit(0)
		memory.add(location)
	return end_coordinates


def moverChooser(facing_direction, steps, end_coordinates):
	if facing_direction == "North":
		end_coordinates = northMover(steps, end_coordinates)
		return end_coordinates
	elif facing_direction == "East":
		end_coordinates = eastMover(steps, end_coordinates)
		return end_coordinates
	elif facing_direction == "South":
		end_coordinates = southMover(steps, end_coordinates)
		return end_coordinates
	else:
		end_coordinates = westMover(steps, end_coordinates)
		return end_coordinates


origin_coordinates = [0, 0]
end_coordinates = [0, 0]
memory = set()

facing_direction = "North"
data = parse('data.txt')
#data = ["R8", "R4", "R4", "R8"]
for entry in data:
	facing_direction = directionChanger(facing_direction, entry[0])
	end_coordinates = moverChooser(facing_direction, entry[1:], end_coordinates)
	print(end_coordinates[0], end_coordinates[1])

print(end_coordinates)
distance = abs(origin_coordinates[0] - end_coordinates[0]) + abs(origin_coordinates[1] - end_coordinates[1])
print(distance)
def solve(data):
	return -1
