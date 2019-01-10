
	
def main():
	move = 1
	x = 0
	y = 0
	count = 1

	n = int(input("What number are we counting to?"))

	while n != count: 

		if move % 2 == 0:
			x, y, count = even(count, move, x, y, n)
			move = move + 1
		else:
			x, y, count = odd(count, move, x, y, n)
			move = move + 1

	print("x: " + str(x))
	print("y: " + str(y))
	
	distance = abs(0 - (x)) + abs(0 - (y))
	print("distance: " + str(distance))
	
	

def even(count, move, x, y, n):
	#print("even")
	x, count = left(x, move, count, n)
	if count == n:
		return x, y, count
	else:
		y, count = down(y, move, count, n)
		return x, y, count
			
					
def odd(count, move, x, y , n):
	#print("odd")
	x, count = right(x, move, count, n)
	if count == n:
		return x, y, count
	else:
		y, count = up(y, move, count, n)
		return x, y, count

		
def right(x, move, count, n):
	#print("right")
	i = 0
	while i < move:
		x = x + 1
		count = count + 1
		
		if count == n:
			return x, count
		else:
			i = i + 1
	
	return x, count
	
def up(y, move, count, n):
	#print("up")
	i = 0
	while i < move:
		y = y + 1
		count = count + 1
		
		if count == n:
			return y, count
		else:
			i = i +1
			
	return y, count

def left(x, move, count, n):
	#print("left")
	i = 0
	while i < move:
		x = x - 1
		count = count + 1
		
		if count == n:
			return x, count
		else:
			i = i + 1
	
	return x, count

def down(y, move, count, n):
	#print("down")
	i = 0
	while i < move:
		y = y - 1
		count = count + 1
		
		if count == n:
			return y, count
		else:
			i = i + 1
			
	return y, count
	
if __name__ == '__main__':
	main()
