import re
from collections import Counter

ans = 0

with open("input04.txt") as f:
	for line in f:
		numstart = re.search("\d", line).start()
		numend = line.find("[")
		str = "".join(sorted(line[:numstart-1].replace("-","")))
		id = int(line[numstart:numend])
		checksum = line[numend+1:len(line)-2]
		most_common = "".join([i[0] for i in Counter(str).most_common(5)])
		if most_common == checksum:
			ans += id
print(ans)
