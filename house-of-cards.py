def getNumberOfCards(x):
    return (3*pow(x, 2) + x) // 2


height = int(input())
while (getNumberOfCards(height) % 4 != 0):
    height += 1
        
print(height)