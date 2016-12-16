# script for dinosaur

dino_dict = {}

with open("dataset1.txt") as f1:
	for line in f1:
		row = line.strip().split(', ')
		dino_dict[row[0]] = {'speed': int(row[1]), 'food': row[2]}

with open("dataset2.txt") as f2:
	for line in f2:
		row = line.strip().split(', ')
		if row[0] in dino_dict:
			dino_dict[row[0]].update({'feature': row[1], 'stance': row[2]})
		else:
			dino_dict[row[0]] = {'speed': 0, 'food': 'default', 'feature': row[1], 'stance': row[2]}

stance2_list = list(filter(lambda x: x[1]['stance'] == '2', dino_dict.items()))
print(stance2_list)

sorted_speed_list = sorted(stance2_list, key=lambda x: -int(x[1]['speed']))
print(sorted_speed_list)
