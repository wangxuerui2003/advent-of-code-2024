with open("input.txt", "r") as f:
	disk = f.read().strip()

max_id = len(disk) // 2

i = 0
j = len(disk) - 1
if len(disk) % 2 == 0:
	j -= 1
iid = 0
jid = max_id
new_id = 0

checksum = 0

def update_checksum(free_space, remain, id):
	global checksum
	global new_id
	if remain > free_space:
		for _ in range(free_space):
			# print(f"{new_id} * {id}")
			checksum += new_id * id
			new_id += 1
		return 0, remain - free_space
	else:
		for _ in range(remain):
			# print(f"{new_id} * {id}")
			checksum += new_id * id
			new_id += 1
		return free_space - remain, 0

trailing_free_space = 0
j_remain = int(disk[j])
while i < j and iid < jid:
	block_size = int(disk[i])
	update_checksum(block_size, block_size, iid)
	i += 1
	free_space = int(disk[i])
	i += 1
	iid += 1
	free_space, j_remain = update_checksum(free_space, j_remain, jid)
	while free_space > 0:
		free_space, j_remain = update_checksum(free_space, j_remain, jid)
		if j_remain == 0:
			jid -= 1
			j -= 1
			trailing_free_space += int(disk[j])
			j -= 1
			j_remain = int(disk[j])

if j_remain != 0:
	update_checksum(trailing_free_space, j_remain, jid)

# print()
# print(new_id)

print(checksum)