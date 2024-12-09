antennas_list = []

with open("input.txt", 'r') as f:
	lines = f.readlines()

	rows = len(lines)
	cols = len(lines[0]) - 1

	for i in range(rows):
		for j in range(cols):
			if lines[i][j].isalnum():
				antennas_list.append((i, j))

antinodes_set = set()

def get_antennas_dx_dy(ant1, ant2):
	return (ant1[1] - ant2[1]), (ant1[0] - ant2[0])

def is_in_map(coord):
	return coord[0] >= 0 and coord[1] >= 0 and coord[0] < rows and coord[1] < cols

for i in range(len(antennas_list)):
	for j in range(i + 1, len(antennas_list)):
		ant1 = antennas_list[i]
		ant2 = antennas_list[j]
		if lines[ant1[0]][ant1[1]] != lines[ant2[0]][ant2[1]]:
			continue
		dx, dy = get_antennas_dx_dy(ant1, ant2)
		anti1 = (ant1[0] + dy, ant1[1] + dx)
		anti2 = (ant2[0] - dy, ant2[1] - dx)

		if is_in_map(anti1):
			antinodes_set.add(anti1)
		if is_in_map(anti2):
			antinodes_set.add(anti2)

print(len(antinodes_set))