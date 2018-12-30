
import json
from pprint import pprint

with open('data.json') as f:
	data = json.load(f)

def arrayChecker(array, count):
	for entry in array:
		if type(entry) == int:
			count += entry
		elif type(entry) == list:
			count = arrayChecker(entry, count)
		elif type(entry) == dict:
			count = typeChecker(entry, count)
	return count

def typeChecker(data, count):
	if type(data) == dict:
		for value in data.values():
			if value == "red":
				return count
		for entry in data:
			if type(entry) == str:
				temp = data[entry]
				count = typeChecker(temp, count)
			elif type(entry) == int:
				count += entry
			elif type(entry) == list:
				count = arrayChecker(entry, count)

	elif type(data) == int:
		count += data
	elif type(data) == list:
		count = arrayChecker(data, count)
	return count 


count = 0
answer = typeChecker(data, count)
print(answer)
