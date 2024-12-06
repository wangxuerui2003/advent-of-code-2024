import re

pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

with open('input.txt', 'r') as f:
	memory = f.read()

result = 0

dos = memory.split('do()')
for do in dos:
	do = do.split("don't()")[0]
	matches = re.findall(pattern, do)

	for match in matches:
		left, right = match.split(',')
		left = int(left[4:])
		right = int(right[:-1])
		result += left * right

print(result)