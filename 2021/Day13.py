# Advent Of coding 
# Day 13
#
# By Shivoy Arora

""" Function to fold the transparent paper """
def folding(i):
    global coordSystem
    global folds

    axis = folds[i][0]
    val = folds[i][1]

    if axis == "y":
        for i in range(len(coordSystem[val])):
            coordSystem[val][i] = "-"
            
        for i in range(len(coordSystem)):
            for j in range(len(coordSystem[i])):
                if coordSystem[val + (val-i)][j] == "#":
                    coordSystem[i][j] = "#"

        for _ in range(val, len(coordSystem)):
            coordSystem.pop(val)

    if axis == "x":
        for i in range(len(coordSystem)):
            coordSystem[i][val] = "|"

        for i in range(len(coordSystem)):
            for j in range(len(coordSystem[i])):
                if coordSystem[i][val + (val-j)] == "#":
                    coordSystem[i][j] = "#"
        
        for i in range(len(coordSystem)):
            for _ in range(val, len(coordSystem[i])):
                coordSystem[i].pop(val)

""" Main Function """
file = open("input/input13.txt", "r")
# file = open("input/test.txt", "r")

readings = file.readlines()

maxY = 0
maxX = 0

coords = []
folds = []

for i in range(len(readings)):
    if readings[i].strip() == "":
        break

    pair = readings[i].strip().split(",")

    if int(pair[0]) > maxX:
        maxX = int(pair[0])
    if int(pair[1]) > maxY:
        maxY = int(pair[1])

    coords.append([int(pair[0]), int(pair[1])])

for j in range(i, len(readings)):
    if readings[j].strip() != "":
        pair = readings[j].split()[2].split("=")
        folds.append([pair[0], int(pair[1])])

# making the coordinate system
coordSystem = [[" " for _ in range(maxX+1)] for _ in range(maxY+1)]

for x, y in coords:
    coordSystem[y][x] = "#"

# Part 1
folding(0)

ctr = 0

for i in coordSystem:
    for j in i:
        if j == "#":
            ctr += 1

print("Part 1")
print("Count:", ctr)

print()

# Part 2
for i in range(1, len(folds)):
    folding(i)

print("Part 2")

for i in coordSystem:
    for j in i:
        print(j,end="")
    print()
