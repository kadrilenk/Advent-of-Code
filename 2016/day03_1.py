f = open("input03.txt")

ans = 0

for line in f:
	num1 = int(line.split()[0])
	num2 = int(line.split()[1])
	num3 = int(line.split()[2])
	if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
		ans += 1
print(ans)
