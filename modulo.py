input_ = []
for _ in range(10):
    input_ += [int(input())]

modulused = (map(lambda y: y % 42, input_))
length = len(set(modulused))
print(length)
