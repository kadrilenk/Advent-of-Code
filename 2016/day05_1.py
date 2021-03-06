import hashlib

key = "cxdnnyjw"
counter = 0
ans = ""

while True:
	input = key + str(counter)
	hash = hashlib.md5((input).encode('utf-8')).hexdigest()
	if hash.startswith('00000'):
		ans += hash[5]
		counter += 1
		if len(ans) == len(key):
			break
	else:
		counter += 1

print(ans)
