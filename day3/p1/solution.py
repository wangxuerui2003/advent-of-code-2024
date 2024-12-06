import re

pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

with open('input.txt', 'r') as f:
	memory = f.read()

matches = re.findall(pattern, memory)

print(matches)

result = 0

for match in matches:
	left, right = match.split(',')
	left = int(left[4:])
	right = int(right[:-1])
	result += left * right

print(result)