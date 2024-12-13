from dataclasses import dataclass
import re
import numpy as np

A_COST = 3
B_COST = 1
ERROR = 10000000000000

@dataclass
class Prize:
	A: tuple[int, int]
	B: tuple[int, int]
	prize: tuple[int, int]

input: list[Prize] = []

# solve simultaneous equation?
'''
94x + 22y = 8400
34x + 67y = 5400
'''

with open("input.txt", "r") as f:
	content = f.read()
	sections = content.split("\n\n")
	for section in sections:
		matches = re.findall(r'X[+=](\d+), Y[+=](\d+)', section)
		a = (int(matches[0][0]), int(matches[0][1]))
		b = (int(matches[1][0]), int(matches[1][1]))
		prize = (int(matches[2][0]) + ERROR, int(matches[2][1]) + ERROR)
		input.append(Prize(a, b, prize))

total_cost = 0

for section in input:
	left = np.array([[section.A[0], section.B[0]], [section.A[1], section.B[1]]])
	right = np.array(list(section.prize))
	solution = np.linalg.solve(left, right)
	# print(solution[0], solution[1])
	if solution[0] < 0 or solution[1] < 0:
		continue
	rounded_x = round(solution[0])
	rounded_y = round(solution[1])
	if (rounded_x * section.A[0] + rounded_y * section.B[0] == section.prize[0]) and (rounded_x * section.A[1] + rounded_y * section.B[1] == section.prize[1]):
		total_cost += solution[0] * A_COST + solution[1] * B_COST
	# print(solution)
	# print(total_cost)

print(int(total_cost))
