import bisect

line = input()
while line != "0 0":
    jack_size, jill_size = [int(i) for i in line.split(' ')]
    jack_collection = []
    in_common = 0
    
    for _ in range(jack_size):
        jack_collection.append(int(input()))

    for _ in range(jill_size):
        value = int(input())
        if bisect.bisect_left(jack_collection, value):
            in_common += 1

    print(in_common)
    line = input()