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
	add = current_result + numbers[current_index]
	mul = current_result * numbers[current_index]
	comb = int(str(current_result) + str(numbers[current_index]))
	if current_index == len(numbers) - 1:
		if add == target:
			return True
		elif mul == target:
			return True
		elif comb == target:
			return True
	add_res = solveable(equation, current_index + 1, add)
	if add_res:
		return True
	mul_res = solveable(equation, current_index + 1, mul)
	if mul_res:
		return True
	comb_res = solveable(equation, current_index + 1, comb)
	if comb_res:
		return True
	return False

solveable_sum = 0

for equation in equations:
	if solveable(equation, 1, equation['numbers'][0]):
		solveable_sum += equation['result']

print(solveable_sum)