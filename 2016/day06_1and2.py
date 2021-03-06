from collections import Counter

with open("input06.txt") as f:
	lines = f.readlines()
	columnn = 0
	list = []
	ans1 = ""
	ans2 = ""
	for i in range(8):
		for line in lines:
			list.append(line[columnn])
		ans1 += Counter("".join(list)).most_common(1)[0][0]
		ans2 += Counter("".join(list)).most_common(1000)[-1][0]
		list = []
		columnn += 1
print("Part 1:", ans1)
print("Part 2:", ans2)
