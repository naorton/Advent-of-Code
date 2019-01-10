
def main():
	
	file = open("Day4.txt", "r")
	passphrases = []
	valid_passphrases = []
	temp = []
	sorted_words = []
	count1 = 0
	count2 = 0
	for line in file:
		
		passphrase = line.split()
		
		passphrases.append(passphrase)

		
	for passphrase in passphrases:
		
		if len(passphrase) == len(set(passphrase)):
			
			valid_passphrases.append(passphrase)
			count1 = count1 + 1		
		
	for passphrase in valid_passphrases:
		temp.clear()
		sorted_words.clear()
		for word in passphrase:
			#print(word)
			sorted_word = sorted(word)
			temp.append(sorted_word)
		
		
		for word in temp:
			a = ''.join(word)
			sorted_words.append(a)
			
		if len(sorted_words) == len(set(sorted_words)):
			count2 = count2 + 1
	
	print(count1)
	print(count2)
if __name__ == '__main__':
	main()