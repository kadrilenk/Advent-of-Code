import re
nlist = ["ab", "cd", "pq", "xy"]
with open('input05.txt') as f:
	lines = f.readlines()
	vowels = 0
	list = []
	for line in lines:
		for i in line:
			if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
				vowels += 1
		if vowels > 2:
			vowels = 0
			if len((re.findall(r"(\w)\1", line))) >= 1:
				if any(x in line for x in nlist):
					pass
				else:
					list.append(line)
			else:
				pass
		else:
			vowels = 0
			pass
	print("Part 1:", len(list))
	list = []
	
	for line in lines:
		if len((re.findall(r"^.*?([a-z]{2}).*?(\1).*$", line))) >= 1:
			if len((re.findall(r"^.*?([a-z]{1}).{1}(\1).*$", line))) >= 1:
				list.append(line)
			else:
				pass
		else:
			pass
	print("Part 2:", len(list))