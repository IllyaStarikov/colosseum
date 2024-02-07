input()
temperatures = [int(i) for i in input().split()]

greaterThanZero = list(filter(lambda x: x < 0, temperatures))
print(len(greaterThanZero))