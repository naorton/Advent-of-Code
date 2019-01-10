

def main():
	n = 0
	steps = 0
	maze = []
	file = open("Day5.txt", "r")
	
	for line in file:
	
		maze.append(int(line.rstrip()))
		
		
	while n >= 0 and n < len(maze):
	
		if maze[n] >= 3:
			jump = maze[n]
			maze[n] = maze[n] - 1
			n = n + jump
		else:
			jump = maze[n]
			maze[n] = maze[n] + 1
			n = n + jump
		steps = steps + 1
		
	print(steps)
	print(len(maze))
	

	
	
if __name__ == '__main__':
	main()