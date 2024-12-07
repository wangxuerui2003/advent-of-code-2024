from collections import Counter

map = []

with open("input.txt", "r") as f:
	map = [line.strip() for line in f.readlines()]

rows = len(map)
cols = len(map[0])

dir = [-1, 0]
original_dir = dir
guard_pos = []

obs_positions = []

for i in range(rows):
	for j in range(cols):
		if map[i][j] == '^':
			guard_pos = [i, j]
		elif map[i][j] == '#':
			obs_positions.append((i, j))

path = set()

def get_next_tile_pos(i, j, dir):
	return i + dir[0], j + dir[1]

def turn_right(dir):
	dirs = [[0,1], [1,0], [0,-1], [-1,0]]
	index = dirs.index(dir)
	return dirs[(index + 1) % len(dirs)]

i, j = guard_pos
while True:
	try:
		path.add((i, j))
		if i >= rows or i < 0 or j >= cols or j < 0:
			break
		ni, nj = get_next_tile_pos(i, j, dir)
		if map[ni][nj] == '#':
			dir = turn_right(dir)
		else:
			i += dir[0]
			j += dir[1]
	except IndexError:
		break

path = list(path)

# todo: how to detect loop

def is_loop(recent_steps):
	counter = Counter(recent_steps)

	# Find the element with the highest occurrence
	most_common = counter.most_common(1)
	if len(most_common) == 0:
		return False
	most_common_element, highest_count = most_common[0]
	if highest_count >= 3:
		return True
	return False

possible_obs = set()

def is_possible_obs(obs_positions, tile):
	for obs in obs_positions:
		if abs(tile[0] - obs[0]) == 1 or abs(tile[1] - obs[1]) == 1:
			return True
	return False
	

for p in path:
	if p == guard_pos:
		continue
	if not is_possible_obs(obs_positions, p):
		continue
	i, j = guard_pos
	dir = original_dir
	loop = False
	turns = {}
	for obs in obs_positions:
		turns[obs] = 0
	turns[p] = 0
	while True:
		try:
			if i >= rows or i < 0 or j >= cols or j < 0:
				break
			ni, nj = get_next_tile_pos(i, j, dir)
			if ni >= rows or ni < 0 or nj >= cols or nj < 0:
				break
			if map[ni][nj] == '#' or (ni, nj) == p:
				turns[(ni, nj)] += 1
				if turns[(ni, nj)] >= 10:
					loop = True
					break
				dir = turn_right(dir)
			else:
				i += dir[0]
				j += dir[1]
		except IndexError as e:
			break

	if loop:
		possible_obs.add(p)

print(len(list(possible_obs)))