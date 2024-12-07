equations: list[dict[int, list[int]]] = []

with open("input.txt", 'r') as f:
	lines = f.readlines()

	for line in lines:
		left, right = line.strip().split(':')
		equation = {
			"result": int(left.strip()),
			"numbers": [int(i) for i in right.strip().split()]
		}
		equations.append(equation)

def solveable(equation, current_index, current_result):
	numbers = equation['numbers']
	target = equation['result']
	if current_index >= len(numbers):
		return False
	if current_result + numbers[current_index] == target:
		return True
	elif current_result * numbers[current_index] == target:
		return True
	plus_res = solveable(equation, current_index + 1, current_result + numbers[current_index])
	if plus_res:
		return True
	mul_res = solveable(equation, current_index + 1, current_result * numbers[current_index])
	if mul_res:
		return True
	return False

solveable_sum = 0

for equation in equations:
	if solveable(equation, 1, equation['numbers'][0]):
		solveable_sum += equation['result']

print(solveable_sum)