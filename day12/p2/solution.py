from dataclasses import dataclass
from copy import deepcopy
from functools import cmp_to_key
from typing import Literal

with open("input.txt", "r") as f:
	garden = [list(row.strip()) for row in f.readlines()]
	rows = len(garden)
	cols = len(garden[0])

def move(pos: tuple[int, int], dir: tuple[int, int]):
	return (pos[0] + dir[0], pos[1] + dir[1])

@dataclass
class Fence:
	pos: tuple[int, int]
	dir: tuple[int, int]

@dataclass
class GardenInfo:
	fences: list[Fence]
	area: int = 0

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
			info.fences.append(Fence(neighbour, dir))
			continue
		if neighbour == prev:
			continue
		if garden[neighbour[0]][neighbour[1]] == target:
			ff_calculate_price(garden, neighbour, pos, info, target)
		elif garden[neighbour[0]][neighbour[1]] != '':
			info.fences.append(Fence(neighbour, dir))

total_price = 0

def get_long_hori_fences(fences: list[Fence]):
	# print(fences)
	i = 0
	fence_reduced = 0
	while i < len(fences):
		row = fences[i].pos[0]
		col = fences[i].pos[1]
		if i < len(fences) - 1 and fences[i + 1].pos[0] == row and abs(fences[i + 1].pos[1] - col) == 1:
			dir = fences[i + 1].pos[1] - col
			while i < len(fences) and fences[i].pos[0] == row and fences[i].pos[1] == col:
				col += dir
				# print(fences[i].pos)
				del fences[i]
				fence_reduced += 1
			fence_reduced -= 1
			i = 0
		else:
			i += 1 
	return fence_reduced

def get_long_vert_fences(fences: list[Fence]):
	# print(fences)
	i = 0
	fence_reduced = 0
	while i < len(fences):
		col = fences[i].pos[1]
		row = fences[i].pos[0]
		if i < len(fences) - 1 and fences[i + 1].pos[1] == col and abs(fences[i + 1].pos[0] - row) == 1:
			dir = fences[i + 1].pos[0] - row
			while i < len(fences) and fences[i].pos[1] == col and fences[i].pos[0] == row:
				row += dir
				# print(fences[i].pos)
				del fences[i]
				fence_reduced += 1
			fence_reduced -= 1
			i = 0
		else:
			i += 1
	return fence_reduced

for i in range(rows):
	for j in range(cols):
		if (i, j) in explored_pos:
			continue
		info = GardenInfo([])
		temp_garden = deepcopy(garden)
		ff_calculate_price(temp_garden, (i, j), None, info, garden[i][j])
		fences = info.fences
		pm = len(fences)
		hori_up = [fence for fence in fences if fence.dir == (-1, 0)]
		hori_down = [fence for fence in fences if fence.dir == (1, 0)]
		vert_left = [fence for fence in fences if fence.dir == (0, -1)]
		vert_right = [fence for fence in fences if fence.dir == (0, 1)]

		hori_up.sort(key=lambda t: (t.pos[0], t.pos[1]))
		fence_reduced = get_long_hori_fences(hori_up)
		pm -= fence_reduced
		
		hori_down.sort(key=lambda t: (t.pos[0], t.pos[1]))
		fence_reduced = get_long_hori_fences(hori_down)
		pm -= fence_reduced

		vert_left.sort(key=lambda t: (t.pos[1], t.pos[0]))
		fence_reduced = get_long_vert_fences(vert_left)
		pm -= fence_reduced
		
		vert_right.sort(key=lambda t: (t.pos[1], t.pos[0]))
		fence_reduced = get_long_vert_fences(vert_right)
		pm -= fence_reduced

		total_price += info.area * pm
		print(f"{info.area} * {pm}")

print(total_price)