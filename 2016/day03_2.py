column = 0
ans = 0

for i in range(3):
	l1 = 0
	l2 = 1
	l3 = 2
	f = open("input03.txt")
	lines = f.readlines()
	for i in range(533):
		num1 = int(lines[l1].split()[column])
		num2 = int(lines[l2].split()[column])
		num3 = int(lines[l3].split()[column])
		if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
			ans += 1
		l1 += 3
		l2 += 3
		l3 += 3
	column += 1
print(ans)
