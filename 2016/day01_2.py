f = open("input01.txt")
for line in f:
	directions = line.split(", ")

x = 0
y = 0
facing = "north"
visited = [(0, 0)]

for i in directions:
    dir = i[0]
    steps = int(i[1:])
    if facing == "north":
        if dir == "R":
            for i in range(steps):
                coord = (x+1, y)
                if coord not in visited:
                    visited.append(coord)
                    x += 1
                else:
                    print("END:", abs(x+1) + abs(y))
                    break
            facing = "east"
        else:
            for i in range(steps):
                coord = (x-1, y)
                if coord not in visited:
                    visited.append(coord)
                    x -= 1
                else:
                    print("END:", abs(x-1) + abs(y))
                    break
            facing = "west"
    elif facing == "east":
        if dir == "R":
            for i in range(steps):
                coord = (x, y-1)
                if coord not in visited:
                    visited.append(coord)
                    y -= 1
                else:
                    print("END:", abs(x) + abs(y-1))
                    break
            facing = "south"
        else:
            for i in range(steps):
                coord = (x, y+1)
                if coord not in visited:
                    visited.append(coord)
                    y += 1
                else:
                    print("END:", abs(x) + abs(y+1))
                    break
            facing = "north"
    elif facing == "south":
        if dir == "R":
            for i in range(steps):
                coord = (x-1, y)
                if coord not in visited:
                    visited.append(coord)
                    x -= 1
                else:
                    print("END:", abs(x-1) + abs(y))
                    break
            facing = "west"
        else:
            for i in range(steps):
                coord = (x+1, y)
                if coord not in visited:
                    visited.append(coord)
                    x += 1
                else:
                    print("END:", abs(x+1) + abs(y))
                    break
            facing = "east"
    elif facing == "west":
        if dir == "R":
            for i in range(steps):
                coord = (x, y+1)
                if coord not in visited:
                    visited.append(coord)
                    y += 1
                else:
                    print("END:", abs(x) + abs(y+1))
                    break
            facing = "north"
        else:
            for i in range(steps):
                coord = (x, y-1)
                if coord not in visited:
                    visited.append(coord)
                    y -= 1
                else:
                    print("END:", abs(x) + abs(y-1))
                    break
            facing = "south"
#print(visited)
#print(abs(x) + abs(y))
