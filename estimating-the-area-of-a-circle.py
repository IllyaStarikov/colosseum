from math import pi

moreInput = True
values = []

while moreInput:
	r, m, c = [float(i) for i in input().split()]
	
	if int(r) + int(m) + int(c) == 0:
		moreInput = False
	else:
		values.append([r, m, c])
# to get the estimate we simply take the ratio of how many land
# to how many were tried, which gets us the ratio of the circle 
# compared to the square and that gives us an approximation
# the real area is pi r^2
for r, m, c in values:
	estimate = c/m * pow(r*2, 2) 
	real = pi * pow(r, 2); 

	print(real, estimate)