import re
from collections import Counter

with open("input04.txt") as f:
	for line in f:
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		numstart = re.search("\d", line).start()
		numend = line.find("[")

		room_name = line[:numstart-1].replace("-"," ")
		id = int(line[numstart:numend])

		crypt_list = []
		decrypt_list = []
		msg = ""

		for letter in room_name:
			if letter.isalpha():
				crypt_list.append(alphabet.index(letter))
			else:
				crypt_list.append(" ")

		for i in crypt_list:
			if type(i) == int:
				decrypt_list.append((i + id) % 26)
			else:
				decrypt_list.append(" ")

		for i in decrypt_list:
			if type(i) == int:
				msg += alphabet[i]
			else:
				msg += " "

		if "north" in msg:
			print(msg, id)
