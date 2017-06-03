def components( num ):
	componentList = []
	while num:
		component = num % 10
		componentList += [component]
		num //= 10

	return componentList

def sumOf( x, sumValue ):
	if not x:
		return sumValue
	else:
		sumValue += x.pop()
		return sumOf(x, sumValue)

def isHappy( num ):
	if num == 0:
		return True
	# else:

	# 	while num:

x = components(1234)
print(sumOf(x, 0))