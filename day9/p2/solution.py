with open("input.txt", "r") as f:
	disk = f.read().strip()

max_id = len(disk) // 2

i = 0
iid = 0
new_id = 0
checksum = 0

def update_checksum(free_space, block_size, id):
	global checksum
	global new_id
	if block_size > free_space:
		for _ in range(free_space):
			# print(f"{new_id} * {id}")
			checksum += new_id * id
			new_id += 1
		return 0, block_size - free_space
	else:
		for _ in range(block_size):
			# print(f"{new_id} * {id}")
			checksum += new_id * id
			new_id += 1
		return free_space - block_size, 0

moved_blocks = set()

while i < len(disk) - 1:
	block_size = int(disk[i])
	if i not in moved_blocks:
		update_checksum(block_size, block_size, iid)
	else:
		new_id += block_size
	i += 1
	free_space = int(disk[i])
	i += 1
	iid += 1
	j = len(disk) - 1
	if len(disk) % 2 == 0:
		j -= 1
	jid = max_id
	while j >= i and free_space > 0:
		if j in moved_blocks:
			jid -= 1
			j -= 2
			continue
		block_size = int(disk[j])
		if free_space >= block_size:
			free_space, _ = update_checksum(free_space, block_size, jid)
			moved_blocks.add(j)
		jid -= 1
		j -= 2
	new_id += free_space

print()
# print(new_id)

print(checksum)