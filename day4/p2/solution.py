with open("input.txt", "r") as f:
	lines = f.readlines()

rows = len(lines)
cols = len(lines[0]) - 1

target = "MAS"

def search_current_mas(row, col):
	if row < 1 or row > rows - 2 or col < 1 or col > cols - 2:
		return 0
	left_diag = lines[row - 1][col - 1] + lines[row][col] + lines[row + 1][col + 1]
	right_diag = lines[row - 1][col + 1] + lines[row][col] + lines[row + 1][col - 1]

	left_valid = left_diag == target or left_diag[::-1] == target
	right_valid = right_diag == target or right_diag[::-1] == target

	return left_valid and right_valid

count = 0

for i in range(rows):
	for j in range(cols):
		if lines[i][j] == 'A':
			count += search_current_mas(i, j)

print(count)
