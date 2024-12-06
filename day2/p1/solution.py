lines = []

with open("input.txt", 'r') as f:
	f_lines = f.readlines()
	for line in f_lines:
		line_splitted = [int(i) for i in line.split()]
		lines.append(line_splitted)

safe_count = 0

for line in lines:
	inc = (line[1] - line[0]) > 0
	safe = True
	for i in range(1, len(line)):
		diff = line[i] - line[i - 1]
		if (diff > 0) != inc:
			safe = False
			break
		if abs(diff) < 1 or abs(diff) > 3:
			safe = False
			break
	if safe:
		safe_count += 1

print(safe_count)
