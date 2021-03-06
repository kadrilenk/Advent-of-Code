f = open("input01.txt")
for line in f:
	directions = line.split(", ")
	
facing = "north"
x = 0
y = 0
	
for i in directions:
	dir = i[0]
	steps = int(i[1:])
	if facing == "north":
		if dir == "R":
			x += steps
			facing = "east"
		elif dir == "L":
			x -= steps
			facing = "west"
	elif facing == "south":
		if dir == "R":
			x -= steps
			facing = "west"
		elif dir == "L":
			x += steps
			facing = "east"
	elif facing == "east":
		if dir == "R":
			y -= steps
			facing = "south"
		elif dir == "L":
			y += steps
			facing = "north"
	elif facing == "west":
		if dir == "R":
			y += steps
			facing = "north"
		elif dir == "L":
			y -= steps
			facing = "south"
			
print(abs(x) + abs(y))
