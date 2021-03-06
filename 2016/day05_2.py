import hashlib

key = "cxdnnyjw"
counter = 0
ans = ["-", "-", "-", "-", "-", "-", "-", "-"]

while "-" in ans:
	input = key + str(counter)
	hash = hashlib.md5((input).encode('utf-8')).hexdigest()
	if hash.startswith('00000'):
		if hash[5].isdigit() and int(hash[5]) < 8 and ans[int(hash[5])] == "-":
			ans[int(hash[5])] = hash[6]
			print("Processing...", "".join(ans))
		counter += 1
	else:
		counter += 1

print("Done:", "".join(ans))
