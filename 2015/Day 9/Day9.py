from Graph import Graph
from collections import defaultdict

data = [entry.strip('\n') for entry in open("data.txt").readlines()]
destinations = []
cities = []
for line in data:
	city1,_,city2,_,_ = line.split()
	if city1 not in cities:
		cities.append(city1)
	if city2 not in cities:
		cities.append(city2)

graph = defaultdict(list)
for line in data:
	temp = line.split()
	destinations.append(temp)
for entry in destinations:
	graph[entry[0]] = []
for entry in destinations:
	graph[entry[0]].append((entry[2], int(entry[4])))

paths = [[] for i in range(7)]
#print(paths)
#print(graph)
count = []
for key in graph:
	print(len(graph[key]))
max_num = 28
while max_num > 0:
	for key in graph:
		for i in range(len(graph[key])):
			paths[i].append(graph[key][i])
			max_num -= 1
#print(paths)

for path in paths:
	temp = 0
	for i in range(len(path)):
		temp += path[i][1]
		i +=1
	count.append(temp)
print(count)
'''		
#print(cities)
destinations = [line.split() for line in data]
#print(destinations)


g = Graph()

for city in cities:
	g.add_node(city)

for entry in destinations:
	g.add_edge(entry[0], entry[2], entry[4])

blah = g.vert_dict['AlphaCentauri']
print(blah)

#print(g.get_vertices())
'''