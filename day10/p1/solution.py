with open("input.txt", "r") as f:
	map = f.readlines()
	int_map = []
	for row in map:
		int_map.append([int(c) for c in row.strip()])
	map = int_map

rows = len(map)
cols = len(map[0])

total_score = 0
current_trail_head_9s = set()

def explore_trails(i, j, prev: tuple[int, int]):
	global total_score
	current_value = map[i][j]
	if i > 0 and map[i - 1][j] - current_value == 1 and (i - 1, j) != prev:
		if map[i - 1][j] == 9:
			current_trail_head_9s.add((i - 1, j))
		else:
			explore_trails(i - 1, j, (i, j))
	if i < rows - 1 and map[i + 1][j] - current_value == 1 and (i + 1, j) != prev:
		if map[i + 1][j] == 9:
			current_trail_head_9s.add((i + 1, j))
		else:
			explore_trails(i + 1, j, (i, j))
	if j > 0 and map[i][j - 1] - current_value == 1 and (i, j - 1) != prev:
		if map[i][j - 1] == 9:
			current_trail_head_9s.add((i, j - 1))
		else:
			explore_trails(i, j - 1, (i, j))
	if j < cols - 1 and map[i][j + 1] - current_value == 1 and (i, j + 1) != prev:
		if map[i][j + 1] == 9:
			current_trail_head_9s.add((i, j + 1))
		else:
			explore_trails(i, j + 1, (i, j))
	
for i in range(rows):
	for j in range(cols):
		if map[i][j] == 0:
			explore_trails(i, j, None)
			total_score += len(current_trail_head_9s)
			current_trail_head_9s = set()

print(total_score)