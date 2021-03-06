f = open("input02.txt")

pos = 5

for line in f:
	for i in line:
		if pos == 1:
			if i == "U":
				pos = 1
			elif i == "D":
				pos = 4
			elif i == "L":
				pos = 1
			elif i == "R":
				pos = 2
		elif pos == 2:
			if i == "U":
				pos = 2
			elif i == "D":
				pos = 5
			elif i == "L":
				pos = 1
			elif i == "R":
				pos = 3
		elif pos == 3:
			if i == "U":
				pos = 3
			elif i == "D":
				pos = 6
			elif i == "L":
				pos = 2
			elif i == "R":
				pos = 3
		elif pos == 4:
			if i == "U":
				pos = 1
			elif i == "D":
				pos = 7
			elif i == "L":
				pos = 4
			elif i == "R":
				pos = 5
		elif pos == 5:
			if i == "U":
				pos = 2
			elif i == "D":
				pos = 8
			elif i == "L":
				pos = 4
			elif i == "R":
				pos = 6
		elif pos == 6:
			if i == "U":
				pos = 3
			elif i == "D":
				pos = 9
			elif i == "L":
				pos = 5
			elif i == "R":
				pos = 6
		elif pos == 7:
			if i == "U":
				pos = 4
			elif i == "D":
				pos = 7
			elif i == "L":
				pos = 7
			elif i == "R":
				pos = 8
		elif pos == 8:
			if i == "U":
				pos = 5
			elif i == "D":
				pos = 8
			elif i == "L":
				pos = 7
			elif i == "R":
				pos = 9
		elif pos == 9:
			if i == "U":
				pos = 6
			elif i == "D":
				pos = 9
			elif i == "L":
				pos = 8
			elif i == "R":
				pos = 9
	print(pos)
