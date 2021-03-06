with open('input01.txt', 'r') as input:
	ans1 = 0
	ans2 = 0
	string = input.read()
	for i in range(0,len(string)):
		if string[i] == "(":
			ans1 += 1
		else:
			ans1 -= 1
			if ans1 < 0 and ans2 == 0:
				ans2 = i + 1
	print("Part 1:", ans1)
	print("Part 2:", ans2)