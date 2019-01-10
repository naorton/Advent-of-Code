#which deer goes the furthest after 2503 seconds
from collections import defaultdict

data = [entry.strip("\n").split() for entry in open("data.txt").readlines()]
#print(data)
deer_info = defaultdict(list)


for entry in data:
	#print(entry[0],entry[3],entry[6],entry[13])
	deer_info[entry[0]] = [int(entry[3])]
	deer_info[entry[0]].append(int(entry[6]))
	deer_info[entry[0]].append(int(entry[13]))

print(deer_info["Vixen"])

def distanceFinder(reindeer, deer_info):
	distance = 0
	time = 0
	race_time = 2503
	while race_time > 0:
		if deer_info[reindeer][1] < race_time:
			distance += deer_info[reindeer][0] * deer_info[reindeer][1]
			#print(distance)
			time += deer_info[reindeer][1]
			time += deer_info[reindeer][2]
			race_time -= time
			#print(race_time)
			time = 0
		else:
			break
	return distance
race_distance = []
for reindeer in deer_info.keys():
	temp = distanceFinder(reindeer, deer_info)
	race_distance.append(temp)

print(race_distance)