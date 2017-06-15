length_of_input = int(input('\n'))

for _ in range(length_of_input):
    cities = set()
    number_of_cities = int(input('\n'))
    
    for _ in range(number_of_cities):
        cities.add(input('\n'))
    print(len(cities))
