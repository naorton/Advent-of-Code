from collections import defaultdict
parsed_data = [entry for entry in open("data.txt").read()]
print(parsed_data)
homes = defaultdict(int)
santa_x = 0
santa_y = 0
robot_x = 0
robot_y = 0
homes[(santa_x, santa_y)] = 2
count = 0
index = 0

for entry in parsed_data:
	if index % 2 == 0:
		if entry == "^":
			santa_y += 1
			homes[(santa_x, santa_y)] += 1
		elif entry == "v":
			santa_y -= 1
			homes[(santa_x, santa_y)] += 1
		elif entry == ">":
			santa_x += 1
			homes[(santa_x, santa_y)] += 1
		elif entry == "<":
			santa_x -= 1
			homes[(santa_x, santa_y)] += 1
	else:
		if entry == "^":
			robot_y += 1
			homes[(robot_x, robot_y)] += 1
		elif entry == "v":
			robot_y -= 1
			homes[(robot_x, robot_y)] += 1
		elif entry == ">":
			robot_x += 1
			homes[(robot_x, robot_y)] += 1
		elif entry == "<":
			robot_x -= 1
			homes[(robot_x, robot_y)] += 1
	index += 1


print(len(homes.values()))
