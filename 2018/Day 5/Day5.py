
original_data = open("data.txt").read()
#print(data)

alphabet = "abcdefghijklmnopqrstuvwxyz"
pairs = [c + c.upper() for c in alphabet]
pairs += [c.upper() + c for c in alphabet]
#print(pairs)

def remove(data):
	for pair in pairs:
		data = data.replace(pair, "")
	return data

def full_remove(data):
	unparsed_data = data
	parsed_data = data
	
	while True:
		parsed_data = remove(unparsed_data)
		if parsed_data == unparsed_data:
			break
		unparsed_data = parsed_data
	return parsed_data


lens = []
for c in alphabet:
	data = original_data
	data = data.replace(c, "")
	data = data.replace(c.upper(), "")
	lens.append(len(full_remove(data)))
print(min(lens))
#fullremove = full_remove(original_data)
#print(fullremove)
#print(len(fullremove))