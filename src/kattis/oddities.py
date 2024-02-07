lines_of_input = int(input())

for _ in range(lines_of_input):
    number = int(input())
    
    if number % 2 == 0:
        print("{0} is even".format(number))
    else:
        print("{0} is odd".format(number))