from collections import defaultdict

def main():
##1 @ 551,185: 21x10
	C = defaultdict(int)
	data = open("Data.txt", "r")

	for line in data:
		words = line.split()
		x, y = words[2].split(',')
		x, y = int(x), int(y[:-1])
		w, h = words[3].split('x')
		w, h = int(w), int(h)
		for dx in range(w):
			for dy in range(h):
				C[(x + dx, y + dy)] += 1
	

	data = open("Data.txt", "r")

	for line in data:
		words = line.split()
		x, y = words[2].split(',')
		x, y = int(x), int(y[:-1])
		w, h = words[3].split('x')
		w, h = int(w), int(h)
		ok = True
		for dx in range(w):
			for dy in range(h):
				if C[(x+dx, y+dy)] > 1:
					ok = False
		if ok:
			print(words[0])



	ans = 0
	for (r,c), v in C.items():
		if v >=2:
			ans += 1
	print(ans)


if __name__ == '__main__':
	main()