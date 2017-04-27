#!/usr/bin/python

from math import sqrt, pow, asin

def calculateY(m, x, b):
	return m*x + b
	
def calculateSlope(one, two):
	return (one[1] - two[1])/(one[0] - two[0])
	
def calculateIntercept(slope, point):
	return point[1] - slope*point[0]

# calulates where the lines of interceptions are
# slope, lineIntercept and radius are floats
# center is a tuple 
# returns bool, point. The bool is if solution exists
# the point is said solution
def getIntercepts(slope, lineIntersept, center, radius):
	determinate = pow(2*lineIntersept*slope - 2*slope*center[1] - 2*center[0], 2) - 4*(pow(slope, 2) + 1)*(pow(lineIntersept, 2) - 2*lineIntersept*center[1] + pow(center[0], 2) + pow(center[1], 2) - pow(radius, 2))
	if determinate >= 0:
		leftHandSide = - 2*lineIntersept*slope + 2*slope*center[1] + 2*center[0]
		denominator = 2*(pow(slope, 2) + 1)
		
		return True, ((leftHandSide + sqrt(determinate))/denominator, (leftHandSide - sqrt(determinate))/denominator)
	else:
		return False, (0, 0)
		

# one and two are both tuples of the form (x, y)
def distance(one, two):
	return sqrt(pow(one[0] - two[0], 2) + pow(one[1] - two[1], 2))
	

treeCount, startX, startY, endX, endY = [float(i) for i in input().split()]

start = (startX, startY)
end = (endX, endY)

trees = []
for i in range(int(treeCount)):
	x, y, radius = [float(i) for i in input().split()]
	trees.append([radius/2, (x, y)])
	
length = distance(start, end)
speed = 200/60 * 1/60 # 200 is base mph, then convert

for radius, center in trees:
	slope = calculateSlope(start, end)
	intercept = calculateIntercept(slope, start)
	intercepts = getIntercepts(slope, intercept, center, radius)

	if intercepts[0]:
		chordLength = distance(
			(intercepts[1][0], calculateY(slope, intercepts[1][0], intercept)), 
			(intercepts[1][1], calculateY(slope, intercepts[1][1], intercept))
		)
		
		alpha = 2*asin(chordLength/(2*radius))
		arcLength = alpha*radius
		
		length -= chordLength
		length += arcLength
		print(length)
		
print(length / speed)
