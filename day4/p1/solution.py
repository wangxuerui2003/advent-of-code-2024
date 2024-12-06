with open("input.txt", "r") as f:
	lines = f.readlines()

rows = len(lines)
cols = len(lines[0]) - 1

target = "XMAS"

def search_word(row, col, dir_row, dir_col):
	for i in range(len(target)):
		if row < 0 or col < 0 or row >= rows or col >= cols:
			return 0
		if lines[row][col] != target[i]:
			return 0
		row += dir_row
		col += dir_col
	return 1

def search_current_x(row, col):
	count = 0
	count += search_word(row, col, 1, 0)
	count += search_word(row, col, 0, 1)
	count += search_word(row, col, -1, 0)
	count += search_word(row, col, 0, -1)
	count += search_word(row, col, 1, 1)
	count += search_word(row, col, 1, -1)
	count += search_word(row, col, -1, 1)
	count += search_word(row, col, -1, -1)
	return count

count = 0

for i in range(rows):
	for j in range(cols):
		if lines[i][j] == 'X':
			count += search_current_x(i, j)

print(count)
