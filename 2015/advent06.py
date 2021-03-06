import re
import numpy as np

grid1 = np.zeros((1000, 1000), 'int32')
grid2 = np.zeros((1000, 1000), 'int32')

with open('input06.txt') as f:
	for line in f:
		
		x0 = int(re.findall(r'\d+', line)[0])
		y0 = int(re.findall(r'\d+', line)[1])
		x1 = int(re.findall(r'\d+', line)[2])
		y1 = int(re.findall(r'\d+', line)[3])
		
		if "turn on" in line:
			grid1[x0:x1+1, y0:y1+1] = 1
			grid2[x0:x1+1, y0:y1+1] += 1
		elif "turn off" in line:
			grid1[x0:x1+1, y0:y1+1] = 0
			grid2[x0:x1+1, y0:y1+1] -= 1
			grid2[grid2 < 0] = 0
		elif "toggle" in line:
			grid1[x0:x1+1, y0:y1+1] = np.logical_not(grid1[x0:x1+1, y0:y1+1])
			grid2[x0:x1+1, y0:y1+1] += 2
							
	print("Part 1:", np.sum(grid1))
	print("Part 2:", np.sum(grid2))