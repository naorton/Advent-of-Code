from Node import Node
from collections import defaultdict

def parse(lines):
	steps = []
	for line in lines:
		line = line.strip("\n")
		line = line.split()
		steps.append((line[1], line[7]))
	return steps

def solve(steps):
    return -1

def find_dependencies(input_dict):
  """Review the steps to create a list of steps that are blocked and unblocked"""
  blocked = []
  for blockers in input_dict.values():
    blocked += blockers
  unblocked = [x for x in list(input_dict.keys()) if x not in blocked]
  return blocked, unblocked


data = open('data.txt').readlines()
graph = defaultdict(list)
steps = parse(data)

for parent, child in steps:
	graph[parent].append(child)

'''
blocked, unblocked = find_dependencies(graph)
print(blocked)
print(unblocked)	
'''
leafs = []

for children in graph.values():
	leafs += children
print(leafs)	
#leafs = list(set(leafs))


roots = list(graph.keys())

for (_key, children) in graph.items():
	for x in children:
		if x in roots:
			roots.remove(x)

#print(leafs)
#print(roots)

order = []

while len(roots) > 0:
	completed = min(roots)
	for i in graph[completed]:
		if i in leafs:
			leafs.remove(i)
		if i not in leafs:
			roots.append(i)
	roots.remove(completed)
	order.append(completed)

print(order)

