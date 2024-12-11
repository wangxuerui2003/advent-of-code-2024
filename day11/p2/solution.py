stones = []

with open("input.txt", "r") as f:
	content = f.read()
	stones = [int(s.strip()) for s in content.split()]

total = len(stones)

memo = {}

TARGET_LAYERS = 75

'''
{
	stone: {
		0: int,
		1: int
		...
		74: int
	}
}
'''

def blink(stone, layer):
	global memo
	if layer >= TARGET_LAYERS:
		return 0
	try:
		return memo[stone][layer]
	except:
		pass
	local_total = 1
	if stone == 0:
		if not memo.get(stone):
			memo[stone] = {}
		memo[stone][layer] = blink(1, layer + 1)
		local_total = memo[stone][layer]
	elif len(str(stone)) % 2 == 0:
		s = str(stone)
		mid = len(s) // 2 + (1 if len(s) % 2 == 1 else 0)
		left, right = int(s[0:mid]), int(s[mid:])
		try:
			if not memo.get(stone):
				memo[stone] = {}
			memo[stone][layer] = memo[left][layer + 1] + memo[right][layer + 1]
			local_total += memo[stone][layer]
		except:
			result = blink(left, layer + 1)
			if not memo.get(left):
				memo[left] = {}
			memo[left][layer + 1] = result
			result = blink(right, layer + 1)
			if not memo.get(right):
				memo[right] = {}
			memo[right][layer + 1] = result
			local_total += memo[left][layer + 1] + memo[right][layer + 1]
	else:
		if not memo.get(stone):
			memo[stone] = {}
		memo[stone][layer] = blink(stone * 2024, layer + 1)
		local_total = memo[stone][layer]
	return local_total

for s in stones:
	total += blink(s, 0)

print(total)