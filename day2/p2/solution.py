import copy

lines = []

with open("input.txt", 'r') as f:
	f_lines = f.readlines()
	for line in f_lines:
		line_splitted = [int(i) for i in line.split()]
		lines.append(line_splitted)

safe_count = 0

def is_safe(line, max_remove):
	removed = 0
	line_copy = None
	line_copy2 = None
	inc = (line[1] - line[0]) > 0
	safe = True
	i = 1
	while i < len(line):
		diff = line[i] - line[i - 1]
		if ((diff > 0) != inc) or (abs(diff) < 1 or abs(diff) > 3):
			if removed >= max_remove:
				safe = False
				break
			if line_copy is None:
				line_copy = copy.deepcopy(line)
				line_copy2 = copy.deepcopy(line)
				del line_copy[i - 1]
				del line_copy2[0]
			del line[i]
			removed += 1
			continue
		i += 1
	if safe:
		return safe
	if line_copy is not None:
		safe = is_safe(line_copy, 0)
		if safe:
			return safe
	if line_copy2 is not None:
		return is_safe(line_copy2, 0)
	return False

for line in lines:
	if is_safe(line, 1):
		safe_count += 1

print(safe_count)
