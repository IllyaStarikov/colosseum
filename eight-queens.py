from functools import reduce

queens = []
sum = 0
for _ in range(8):
	userInput = input()	
	sum += userInput.count('*')
	userInput = userInput.replace(".", "0")
	userInput = userInput.replace("*", "1")
	queens.append(list(userInput))
	
validSolution = True

if sum < 8: 
	validSolution = False

# Horizontals
for i in range(8):
	arrayOfInt = map((lambda x: int(x)), queens[i])
	if reduce((lambda x, y: x + y), arrayOfInt) > 1:
		validSolution = False

# Verticals
for i in range(8):
	array = [row[i] for row in queens]
	arrayOfInt = map((lambda x: int(x)), array)
	if reduce((lambda x, y: x + y), arrayOfInt) > 1:
		validSolution = False
		
# Diagonols
# Ever have a good idea drunk at 3 o'clock in the morning?
# Well, you're looking at it
solutions=[[[0,0,0,0,0,0,1,0],
    		[0,0,0,0,0,0,0,1],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0]]
    		,
    		[[0,0,0,0,0,1,0,0],
    		[0,0,0,0,0,0,1,0],
    		[0,0,0,0,0,0,0,1],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0]]
    		,
    		[[0,0,0,0,1,0,0,0],
    		[0,0,0,0,0,1,0,0],
    		[0,0,0,0,0,0,1,0],
    		[0,0,0,0,0,0,0,1],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0]]
    		,
    		[[0,0,0,1,0,0,0,0],
    		[0,0,0,0,1,0,0,0],
    		[0,0,0,0,0,1,0,0],
    		[0,0,0,0,0,0,1,0],
    		[0,0,0,0,0,0,0,1],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0]]
    		,
    		[[0,0,1,0,0,0,0,0],
    		[0,0,0,1,0,0,0,0],
    		[0,0,0,0,1,0,0,0],
    		[0,0,0,0,0,1,0,0],
    		[0,0,0,0,0,0,1,0],
    		[0,0,0,0,0,0,0,1],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0]]
    		,
    		[[0,1,0,0,0,0,0,0],
    		[0,0,1,0,0,0,0,0],
    		[0,0,0,1,0,0,0,0],
    		[0,0,0,0,1,0,0,0],
    		[0,0,0,0,0,1,0,0],
    		[0,0,0,0,0,0,1,0],
    		[0,0,0,0,0,0,0,1],
    		[0,0,0,0,0,0,0,0]]
    		,
    		[[1,0,0,0,0,0,0,0],
    		[0,1,0,0,0,0,0,0],
    		[0,0,1,0,0,0,0,0],
    		[0,0,0,1,0,0,0,0],
    		[0,0,0,0,1,0,0,0],
    		[0,0,0,0,0,1,0,0],
    		[0,0,0,0,0,0,1,0],
    		[0,0,0,0,0,0,0,1]]
    		,
    		[[0,0,0,0,0,0,0,0],
    		[1,0,0,0,0,0,0,0],
    		[0,1,0,0,0,0,0,0],
    		[0,0,1,0,0,0,0,0],
    		[0,0,0,1,0,0,0,0],
    		[0,0,0,0,1,0,0,0],
    		[0,0,0,0,0,1,0,0],
    		[0,0,0,0,0,0,1,0]]
    		,
    		[[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[1,0,0,0,0,0,0,0],
    		[0,1,0,0,0,0,0,0],
    		[0,0,1,0,0,0,0,0],
    		[0,0,0,1,0,0,0,0],
    		[0,0,0,0,1,0,0,0],
    		[0,0,0,0,0,1,0,0]]
    		,
    		[[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[1,0,0,0,0,0,0,0],
    		[0,1,0,0,0,0,0,0],
    		[0,0,1,0,0,0,0,0],
    		[0,0,0,1,0,0,0,0],
    		[0,0,0,0,1,0,0,0]]
    		,
    		[[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[1,0,0,0,0,0,0,0],
    		[0,1,0,0,0,0,0,0],
    		[0,0,1,0,0,0,0,0],
    		[0,0,0,1,0,0,0,0]]
    		,
    		[[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[1,0,0,0,0,0,0,0],
    		[0,1,0,0,0,0,0,0],
    		[0,0,1,0,0,0,0,0]]
    		,
    		[[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[0,0,0,0,0,0,0,0],
    		[1,0,0,0,0,0,0,0],
    		[0,1,0,0,0,0,0,0]]
		,
		[[0,1,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
		,
		[[0,0,1,0,0,0,0,0],
		[0,1,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
		,
		[[0,0,0,1,0,0,0,0],
		[0,0,1,0,0,0,0,0],
		[0,1,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
		,
		[[0,0,0,0,1,0,0,0],
		[0,0,0,1,0,0,0,0],
		[0,0,1,0,0,0,0,0],
		[0,1,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
		,
		[[0,0,0,0,0,1,0,0],
		[0,0,0,0,1,0,0,0],
		[0,0,0,1,0,0,0,0],
		[0,0,1,0,0,0,0,0],
		[0,1,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
		,
		[[0,0,0,0,0,0,1,0],
		[0,0,0,0,0,1,0,0],
		[0,0,0,0,1,0,0,0],
		[0,0,0,1,0,0,0,0],
		[0,0,1,0,0,0,0,0],
		[0,1,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
		,
		[[0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,1,0],
		[0,0,0,0,0,1,0,0],
		[0,0,0,0,1,0,0,0],
		[0,0,0,1,0,0,0,0],
		[0,0,1,0,0,0,0,0],
		[0,1,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0]]
		,
		[[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,1,0],
		[0,0,0,0,0,1,0,0],
		[0,0,0,0,1,0,0,0],
		[0,0,0,1,0,0,0,0],
		[0,0,1,0,0,0,0,0],
		[0,1,0,0,0,0,0,0]]
		,
		[[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,1,0],
		[0,0,0,0,0,1,0,0],
		[0,0,0,0,1,0,0,0],
		[0,0,0,1,0,0,0,0],
		[0,0,1,0,0,0,0,0]]
		,
		[[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,1,0],
		[0,0,0,0,0,1,0,0],
		[0,0,0,0,1,0,0,0],
		[0,0,0,1,0,0,0,0]]
		,
		[[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,1,0],
		[0,0,0,0,0,1,0,0],
		[0,0,0,0,1,0,0,0]]
		,
		[[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,1,0],
		[0,0,0,0,0,1,0,0]]
		,
		[[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,1,0]]]

for array in solutions:
	sum = 0
	for i in range(8):
		for j in range (8):
			sum += array[i][j] & int(queens[i][j])
	if sum > 1:
		validSolution = False
	

if validSolution:
	print("valid")
else:
	print("invalid")

	
