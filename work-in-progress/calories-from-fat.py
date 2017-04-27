import re

conversions = [
	("fat", 9),
	("protein", 4), 
	("sugar", 4),
	("starch", 4),
	("alcohol", 4)
]

def main():
	userInput = input().split(' ')
	measurements = list(map(lambda x: re.search('(\d*)(.)', x), userInput))
	
	summedCalories = 0
	summedPercentage = 0
	
	fatCalories = 0
	fatPercentage = 0
	
	for measurement, (label, caloriesPerGram) in zip(measurements, conversions):
		value = int(measurement.group(1))
		units = measurement.group(2)
		
		if units == 'g':
			summedCalories = value * caloriesPerGram
		elif units == '%':
			summedPercentage += value
		elif units == 'C':
			summedCalories += value
				
		if not fatCalories and not fatPercentage:
			fatCalories += summedCalories
			fatPercentage += summedPercentage	
			
	
	remainingCalories = summedCalories * (    summedPercentage)/100
	remainingPercent = 100 - summedPercentage
	
	caloriesFromFat = fatCalories/100 + fatPercentage
	
	print(caloriesFromFat)
		

		
if __name__ == "__main__":
	main()
