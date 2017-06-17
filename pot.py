lines_of_input = int(input())
sum_ = 0

for _ in range(lines_of_input):
    number = input() 
    base = int(number[:-1])
    exponent = int(number[-1])
    
    sum_ += pow(base, exponent)

print(sum_)
