import collections
data =[entry.strip("\n") for entry in open("data.txt").readlines()] 
#print(data)

entries = collections.defaultdict(list)


for entry in data:
	i = 0
	while i < len(entry):
		entries[i].append(entry[i])
		i += 1

for key in entries:

	print(max(collections.Counter(entries[key])))
