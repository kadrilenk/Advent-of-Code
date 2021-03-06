import hashlib
key = 'yzbqklnj'
number = 0

while True:
	input = key + str(number)
	hash = hashlib.md5((input).encode('utf-8')).hexdigest()
	if hash.startswith('00000'):
		print("Part 1:", number)
		break
	else:
		number += 1


while True:
	input = key + str(number)
	hash = hashlib.md5((input).encode('utf-8')).hexdigest()
	if hash.startswith('000000'):
		print("Part 2:", number)
		break
	else:
		number += 1