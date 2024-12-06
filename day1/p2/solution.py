left = []
right = []

# parse input

with open("input.txt", 'r') as f:
	lines = f.readlines()
	for line in lines:
		l, r = line.split()
		left.append(int(l))
		right.append(int(r))

sim = 0

occurrences_right = {}
for v in right:
	if occurrences_right.get(v, None) is None:
		occurrences_right[v] = 1
	else:
		occurrences_right[v] += 1

for v in left:
	occ_right = occurrences_right.get(v, 0)
	sim += v * occ_right

print(sim)
