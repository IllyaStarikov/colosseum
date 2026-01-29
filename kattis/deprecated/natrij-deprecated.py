import sys

current = [int(i) for i in input().split(':')]
future = [int(i) for i in input().split(':')]

# Although input is given hh:mm:ss, and that's the intuitive way,
# We do time arithmetic based ss:mm:hh, carrying from the next column
# so our format will be ss:mm:hh
current.reverse()
future.reverse()

# Because the future can be a day ahead, we give it another day
# Format is now ss:mm:hh:dd
current.append(0)
future.append(1)

timeFormat = [60, 60, 24, 1]
solution = []

for i, (currentTime, futureTime) in enumerate(zip(current, future)):
	if futureTime < currentTime or futureTime < 0 or currentTime < 0:
		future[i + 1] -= 1
		futureTime += timeFormat[i]
		
	solution.append(futureTime - currentTime)
	
solution.pop()

total = 60*60*solution[2] + 60*solution[1] + 60*solution[0]

if total == 0:
	print("00:00:01")
elif total > 86400:
	print("24:00:00")
else:
	for index, time in enumerate(reversed(solution)):
		if time < 10:
			sys.stdout.write("0" + str(time))
		else:
			sys.stdout.write(str(time))
		
		if index >= 0 and index < len(solution) - 1:
			sys.stdout.write(":")