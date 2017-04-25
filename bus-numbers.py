import sys

def twoConsecutiveIntegers(list, index, atIndex):
	return list[index] == atIndex and list[index + 1] == atIndex + 1

input()

values = [int(i) for i in input().split(' ')]
values.sort()

output = []

for index, value in enumerate(values):
	# If first iteration
	if output == []:
		output.append(value)	
	# if we are in a cycle of appending values
	elif output[-1] == "-":
		if len(values) - (index + 1) < 1 or value + 1 != values[index + 1]:
			output.append(value)
		
	# if we should append values 
	elif output[-1] == value - 1:
		if len(values) - (index + 1) > 0 and twoConsecutiveIntegers(values, index, value):
			output.append("-")
		else:
			output.append(value)
	# If none of the above, just a plain append
	else:
		output.append(value)
		
for index, element in enumerate(output):
	sys.stdout.write(str(element))
	if len(output) - index > 1 and output[index + 1] != '-' != output[index]:
		sys.stdout.write(" ")