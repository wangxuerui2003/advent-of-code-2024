from dataclasses import dataclass
from copy import deepcopy

with open("input.txt", "r") as f:
	garden = [list(row.strip()) for row in f.readlines()]
	rows = len(garden)
	cols = len(garden[0])

def move(pos: tuple[int, int], dir: tuple[int, int]):
	return (pos[0] + dir[0], pos[1] + dir[1])

@dataclass
class GardenInfo:
	area: int = 0
	pm: int = 0

explored_pos = set()

# ff: floodfill
# pm: perimeter
def ff_calculate_price(garden: list[list[str]], pos: tuple[int, int], prev: tuple[int, int], info: GardenInfo, target):
	info.area += 1
	explored_pos.add(pos)
	garden[pos[0]][pos[1]] = ''
	dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
	for dir in dirs:
		neighbour = move(pos, dir)
		if neighbour[0] < 0 or neighbour[0] >= rows or neighbour[1] < 0 or neighbour[1] >= cols:
			info.pm += 1
			continue
		if neighbour == prev:
			continue
		if garden[neighbour[0]][neighbour[1]] == target:
			ff_calculate_price(garden, neighbour, pos, info, target)
		elif garden[neighbour[0]][neighbour[1]] != '':
			info.pm += 1

total_price = 0

for i in range(rows):
	for j in range(cols):
		if (i, j) in explored_pos:
			continue
		info = GardenInfo()
		temp_garden = deepcopy(garden)
		ff_calculate_price(temp_garden, (i, j), None, info, garden[i][j])
		total_price += info.area * info.pm
		# print(f"{info.area} * {info.pm}")

print(total_price)