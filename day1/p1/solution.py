left = []
right = []

# parse input

with open("input.txt", 'r') as f:
	lines = f.readlines()
	for line in lines:
		l, r = line.split()
		left.append(int(l))
		right.append(int(r))

left.sort()
right.sort()

distance = 0

for l, r in zip(left, right):
	distance += abs(r - l)

print(distance)