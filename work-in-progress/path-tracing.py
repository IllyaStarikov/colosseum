import sys

moves = sys.stdin.read()
moves = moves.split('\n')

path = [[' ' for x in range(abs(moves.count("left") - moves.count("right")))] for y in range(abs(moves.count("up") - moves.count("down")))]

startY = moves.count("up") + moves.count("down") - max(moves.count("down"), moves.count("up"))
startX = moves.count("left") + moves.count("right") - max(moves.count("left"), moves.count("right"))

location = (startX, startY) # of the form (x, y)
path[location[0]][location[1]] = 'S'

print(startX)
print(startY)

for move in moves:
    if move == "up":
        location = (location[0], location[1] + 1)
    elif move == "down":
        location = (location[0], location[1] - 1)
    elif move == "left":
        location = (location[0] - 1, location[1])
    elif move == "right":
        location = (location[0] + 1, location[1])

    path[location[0]][location[1]] = '*'

path[location[0]][location[1]] = 'E'

print(path)
