import sys

# list MUST be in ther format [hh, mm, ss]
def listToSeconds(hours, minutes, seconds):
	return hours*60*60 + minutes*60 + seconds

def secondsToHoursMinuteSeconds(seconds):
	hours = int(seconds / (60*60))
	minutes = int((seconds - hours*60*60)/60)
	seconds = seconds % 60
	return [hours, minutes, seconds]

current = [int(i) for i in input().split(':')]
future = [int(i) for i in input().split(':')]

totalSecondsInCurrent = listToSeconds(current[0], current[1], current[2])
totalSecondsInFuture = listToSeconds(future[0], future[1], future[2])

solutionInSeconds = totalSecondsInFuture - totalSecondsInCurrent

if solutionInSeconds < 0:
	solutionInSeconds += listToSeconds(24, 0, 0)

if solutionInSeconds == 0:
	solutionInSeconds += listToSeconds(24, 0, 0)
	
for index, time in enumerate(secondsToHoursMinuteSeconds(solutionInSeconds)):
	if time < 10:
		sys.stdout.write("0" + str(time))
	else:
		sys.stdout.write(str(time))
	
	if index >= 0 and index < len(secondsToHoursMinuteSeconds(solutionInSeconds)) - 1:
		sys.stdout.write(":")