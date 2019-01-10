
data = [entry.strip("\n") for entry in open("data.txt").readlines()]
#word = "ugknbfddgicrmopn"
def numVowels(word):
	vowels = "aeiou"
	num_vowels = 0
	for letter in word:
		for vowel in vowels:
			if letter == vowel:
				num_vowels += 1
	return num_vowels

def doubleLetter(word):
	doubleLetters = 0
	i = 0
	while i < (len(word)-1):
		if word[i] == word[i+1]:
			doubleLetters += 1
		i += 1
	return doubleLetters

def naughtyString(word):
	naughty_strings = ["ab", "cd", "pq", "xy"]
	i = 0
	while i < (len(word)-1):
		temp = word[i:i+2]
		for entry in naughty_strings:
			if temp == entry:
				return True
		i += 1
	return False
nice_strings = 0
for word in data:
	num_vowels = numVowels(word)
	doubleLetters = doubleLetter(word)
	naughty_string = naughtyString(word)

	if num_vowels >= 3:
		if doubleLetters >= 1:
			if naughty_string == False:
				nice_strings += 1

print(nice_strings)

'''
nice_strings = 0
num_vowels = numVowels(word)
print(num_vowels)
doubleLetters = doubleLetter(word)
print(doubleLetters)
naughty_string = naughtyString(word)
print(naughty_string)
if num_vowels >= 3:
		if doubleLetters >= 1:
			if naughty_string == False:
				nice_strings += 1
print(nice_strings)
'''