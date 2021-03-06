import re

ans1, ans2 = 0, 0

with open("input07.txt") as f:
	for line in f:
		criteria1 = r"\[\w*(.)(.)\2\1\w*\]"
		criteria2 = r"\w*(?!(.)\1\1\1)(.)(.)\3\2\w*\["
		criteria3 = r"\]\w*(?!(.)\1\1\1)(.)(.)\3\2\w*"

		if re.search(criteria1, line):
			pass
		elif re.search(criteria2, line) or re.search(criteria3, line):
			ans1 += 1

		criteria4 = r"(.)(.)\1\w*\[\w*\2\1\2"
		criteria5 = r"(.)(.)\1\w*\[\S*\[\w*\2\1\2"
		criteria6 = r"(.)(.)\1\w*\]\w*\2\1\2"
		criteria7 = r"(.)(.)\1\w*\]\S*\]\w*\2\1\2"

		if re.search(criteria4, line) or re.search(criteria5, line) or re.search(criteria6, line) or re.search(criteria7, line):
			ans2 += 1

print("Part 1:", ans1) #115
print("Part 2:", ans2) #231
