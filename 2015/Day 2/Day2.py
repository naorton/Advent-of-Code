
parsed_data = [entry.strip('\n') for entry in open("data.txt").readlines()]
print(parsed_data)

total = 0
ribbon = 0

for entry in parsed_data:
	length, width, height = entry.split("x")
	length = int(length)
	width = int(width)
	height = int(height)
	perimeter_lengths = [length, width, height]
	perimeter_lengths.remove(max(perimeter_lengths))
	perimeter = (perimeter_lengths[0]*2) + (perimeter_lengths[1]*2)
	surface_area = (2*length*width) + (2*width*height) + (2*height*length)
	cubic_feet = (length*width*height)
	areas = [length*width, width*height, height*length]
	total += (surface_area + min(areas))
	ribbon += (perimeter+cubic_feet)

print(total)
print(ribbon)
