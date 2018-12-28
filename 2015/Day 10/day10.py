#data = [1113222113]

#1 = 11
#11 = 21
#21 = 1211
#1211 = 111221
#111221 = 312211

data = [1,1]

count = 0

temp = len(data) + 1

final = []
final.append(temp)
final += data
print(final)

def num_count(num_list):
	temp_list = []
	count = 1
	temp_num = num_list[0]
	i = 1
	if len(num_list) == 1:
		temp_list.append(count)
		temp_list.append(temp_num)
		return temp_list
	while i < len(num_list):
		if num_list[i-1] == num_list[i]:
			count += 1
		elif num_list[i-1] != num_list[i]:
			temp_list.append(count)
			temp_list.append(temp_num)
			temp_num = num_list[i]
			count = 1
		if i+1 == len(num_list):
			temp_list.append(count)
			temp_list.append(temp_num)
		i += 1

	return temp_list

data = [1,1,1,3,2,2,2,1,1,3]
i = 0
new_list = data
while i < 50:
	new_list = num_count(new_list)
	i +=1
print(len(new_list))