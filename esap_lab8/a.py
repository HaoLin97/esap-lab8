import numpy as np
arr = []
for i in range(0,4):
	x = np.random.randint(0,8)
	y = np.random.randint(0,8)
	c = (x,y)
	arr.append(c)

print(arr)
