x = y = 0
list1 = [[0,0]]
with open('input03.txt') as f:
	line = f.readline()
	for char in line:
		cord = []
		if char == "^":
			y += 1
			cord.extend([x,y])
		elif char == "v":
			y -= 1
			cord.extend([x,y])
		elif char == ">":
			x += 1
			cord.extend([x,y])
		elif char == "<":
			x -= 1
			cord.extend([x,y])
			
		if cord not in list1:
			list1.append(cord)
	print("Part 1:", len(list1))
	
	n = x0 = y0 = x1 = y1 = 0
	list2 = [[0,0]]
	while len(line) > n:
		cord0 = []
		cord1 = []
		f.seek(n)
		chars = f.read(2)
		n +=2
		
		if chars[0] == "^":
			y0 += 1
			cord0.extend([x0,y0])
		elif chars[0] == "v":
			y0 -= 1
			cord0.extend([x0,y0])
		elif chars[0] == ">":
			x0 += 1
			cord0.extend([x0,y0])
		elif chars[0] == "<":
			x0 -= 1
			cord0.extend([x0,y0])
		if cord0 not in list2:
			list2.append(cord0)
		
		if chars[1] == "^":
			y1 += 1
			cord1.extend([x1,y1])
		elif chars[1] == "v":
			y1 -= 1
			cord1.extend([x1,y1])
		elif chars[1] == ">":
			x1 += 1
			cord1.extend([x1,y1])
		elif chars[1] == "<":
			x1 -= 1
			cord1.extend([x1,y1])
		if cord1 not in list2:
			list2.append(cord1)
	print("Part 2:", len(list2))