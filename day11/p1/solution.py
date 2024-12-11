stones = []

with open("input.txt", "r") as f:
	content = f.read()
	stones = [int(s.strip()) for s in content.split()]

def blink():
	global stones
	new_stones = []
	for stone in stones:
		if stone == 0:
			new_stones.append(1)
		elif len(str(stone)) % 2 == 0:
			s = str(stone)
			mid = len(s) // 2 + (1 if len(s) % 2 == 1 else 0)
			left, right = s[0:mid], s[mid:]
			new_stones.append(int(left))
			new_stones.append(int(right))
		else:
			new_stones.append(stone * 2024)
	stones = new_stones

for i in range(25):
	blink()

print(len(stones))