import re
import numpy as np
gridx, gridy = 6, 50

grid = np.chararray((gridx, gridy), unicode = True)
grid[:] = "."

with open('input08.txt') as f:
	for line in f:
		x = int(re.findall(r'\d+', line)[0]) # column row
		y = int(re.findall(r'\d+', line)[1]) # step
		if "rect" in line:
			grid[0:y, 0:x] = "#"

		elif "rotate column" in line:
			for i in range(y):
				last = grid[gridx-1:gridx, x:x+1][0][0]
				m = gridx
				n = m -1
				for j in range(m):
					grid[m:m+1, x:x+1] = grid[n:n+1, x:x+1]
					m -= 1
					n -= 1
				grid[1-1:1, x:x+1] = last

		elif "rotate row" in line:
			for i in range(y):
				last = grid[x:x+1, gridy-1:gridy][0][0]
				m = gridy
				n = m - 1
				for j in range(n):
					grid[x:x+1, m-1:m] = grid[x:x+1, n-1:n]
					m -= 1
					n -= 1
				grid[x:x+1, 0:1] = last
	print("Pixels lit:", np.sum(np.char.count(grid,"#")))

	code = ""
	for i in range(6):
		for j in range(50):
			code += grid[i][j]
		print(code)
		code = ""
