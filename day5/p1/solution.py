rules = []
inputs = []

with open('input.txt', 'r') as f:
	lines = f.readlines()
	split_index = lines.index("\n")
	rules = [line.strip() for line in lines[:split_index]]
	inputs = [line.strip() for line in lines[split_index + 1:]]

bigger_dict: dict[int, list] = {}

for rule in rules:
	left_num, right_num = [int(i) for i in rule.split('|')]
	if bigger_dict.get(left_num) is None:
		bigger_dict[left_num] = [right_num]
	else:
		bigger_dict[left_num].append(right_num)

middle_sum = 0

for input in inputs:
	valid = True
	pages = [int(i) for i in input.split(',')]
	i = 0
	while i < len(pages) and valid:
		for p in pages[i+1:]:
			if not bigger_dict.get(pages[i]) or (p not in bigger_dict[pages[i]]):
				valid = False
				break
		i += 1
	if valid:
		# print(pages[len(pages) // 2])
		middle_sum += pages[len(pages) // 2]


print(middle_sum)
