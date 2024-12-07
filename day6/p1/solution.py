map = []

with open("input.txt", "r") as f:
	map = [line.strip() for line in f.readlines()]

rows = len(map)
cols = len(map[0])

dir = [-1, 0]
guard_pos = []

for i in range(rows):
	for j in range(cols):
		if map[i][j] == '^':
			guard_pos = [i, j]

path = set()

def get_next_tile(i, j, dir):
	return map[i + dir[0]][j + dir[1]]

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
		elif get_next_tile(i, j, dir) == '#':
			dir = turn_right(dir)
		else:
			i += dir[0]
			j += dir[1]
	except IndexError:
		break
		

print(len(path))
