from math import ceil, log2

number_of_statues = int(input())

if number_of_statues < 2:
    print(number_of_statues)
else:
    print(ceil(log2(number_of_statues)) + 1)
