def second_smallest(element):
    m1, m2 = float('inf'), float('inf')
    for x in element:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

with open('input02.txt') as f:
	paper = 0
	ribbon = 0
	for line in f:
		elements = line.strip().split("x")
		new_list = []
		for item in elements:
			new_list.append(int(item))
		l = int(elements[0])
		w = int(elements[1])
		h = int(elements[2])
		paper += 2*l*w + 2*w*h + 2*h*l + min(l,w,h) * second_smallest(new_list)
		ribbon += l * w * h + 2*min(l,w,h) + 2*second_smallest(new_list)
	print("Part 1:", paper)
	print("Part 2:", ribbon)