from functools import reduce

names = input().split("-")
reduced = reduce((lambda x, y: x + str(y[0])), names, "")

print(reduced)