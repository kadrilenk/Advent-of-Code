import re

str = ""

with open("input09.txt") as f:
	for line in f:
		line = line.strip()
		while len(line) > 0:
			length = int(re.findall(r"\d+", line)[0])
			repeat = int(re.findall(r"\d+", line)[1])
			start = line.find(re.findall(r"\)", line)[0])+1
			extracted = line[start:start+length]
			for i in range(repeat):
				str += extracted
			remaining = line[start+length:]
			if remaining.find(re.findall(r"\(", line)[0]) == -1:
				addition = remaining
			else:
				addition = remaining[:remaining.find(re.findall(r"\(", line)[0])]
			str += addition
			removed = line[:start+length+len(addition)]
			line = line.replace(removed,"")
	print(len(str))
