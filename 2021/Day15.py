# Advent Of coding 
# Day 15
#
# Using Dijkstra's algorithm
# By Shivoy Arora

""" Add risk value of adjacent vertices """
def AddAdj(vertex, risk):
    global notSptSet, dataset
    global readings

    i = vertex[0]
    j = vertex[1]

    try:
        if dataset[i+1][j] != "X" and dataset[i+1][j] < (risk + int(readings[i+1][j])):
            pass
        else:
            # string the min risk to get to that vertex in dataset
            dataset[i+1][j] = risk + int(readings[i+1][j])
            # add that vertex in the set which contains vertices whose risk is know but is not in sptSet
            notSptSet.add((i+1,j))
    except IndexError:
        pass
    try:
        if i > 0:
            if dataset[i-1][j] != "X" and dataset[i-1][j] < (risk + int(readings[i-1][j])):
                pass
            else:
                dataset[i-1][j] = risk + int(readings[i-1][j])
                notSptSet.add((i-1, j))
    except IndexError:
        pass
    try:
        if dataset[i][j+1] != "X" and dataset[i][j+1] < (risk + int(readings[i][j+1])):
            pass
        else:
            dataset[i][j+1] = risk + int(readings[i][j+1])
            notSptSet.add((i, j+1))
    except IndexError:
        pass
    try:
        if j > 0:
            if dataset[i][j-1] != "X" and dataset[i][j-1] < (risk + int(readings[i][j-1])):
                pass
            else:
                dataset[i][j-1] = risk + int(readings[i][j-1])
                notSptSet.add((i,j-1))
    except IndexError:
        pass

""" Add vertex to sptSet with min risk """
def MinRisk():
    global sptSet
    global notSptSet, dataset

    minRisk = None
    minVer = (0,0)

    # checking notSptSet for the next vertex with least risk
    for i in notSptSet:
        if not minRisk or minRisk > dataset[i[0]][i[1]]:
            minRisk = dataset[i[0]][i[1]]
            minVer = (i[0], i[1])

    # removing the vertex from notSptSet which is added to sptSet
    notSptSet.remove(minVer)
    return minVer

""" Main Function """
file = open("input/input15.txt","r")
# file = open("input/test.txt","r")
readings = [i.strip() for i in file.readlines()]

sptSet = [(0,0),]
notSptSet = set()

dataset = [["X" for _ in range(len(readings[0]))] for _ in range(len(readings))]
dataset[0][0] = 0

risk = 0

run = True
while run:
    AddAdj(sptSet[-1], risk)
    minVertex = MinRisk()
    sptSet.append(minVertex)
    risk = dataset[minVertex[0]][minVertex[1]]

    # if the element added to sptSet is the destination then exiting
    if sptSet[-1] == ((len(readings) - 1), (len(readings[-1]) - 1)):
        run = False

print("Part 1")
print("Min Risk:", risk)

print()

# Part 2
#
# Creating the new map
tempReadings = [[int(j) for j in i] for i in readings]

# for one time towards right
for i in range(len(readings)):
    for j in range(len(readings[i])):
        if (int(readings[i][j])+1)%9 == 0:
            tempReadings[i].append(9)
        else:
            tempReadings[i].append((int(readings[i][j])+1)%9)
# Second time
for i in range(len(readings)):
    for j in range(len(readings[i])):
        if (int(readings[i][j])+2)%9 == 0:
            tempReadings[i].append(9)
        else:
            tempReadings[i].append((int(readings[i][j])+2)%9)
# Third time
for i in range(len(readings)):
    for j in range(len(readings[i])):
        if (int(readings[i][j])+3)%9 == 0:
            tempReadings[i].append(9)
        else:
            tempReadings[i].append((int(readings[i][j])+3)%9)
# Fourth time
for i in range(len(readings)):
    for j in range(len(readings[i])):
        if (int(readings[i][j])+4)%9 == 0:
            tempReadings[i].append(9)
        else:
            tempReadings[i].append((int(readings[i][j])+4)%9)

# assigning tempReading to reading
readings = tempReadings.copy()

# for one time downwards
for i in range(len(readings)):
    row = []
    for j in range(len(readings[i])):
        if (int(readings[i][j])+1)%9 == 0:
            row.append(9)
        else:
            row.append((int(readings[i][j])+1)%9)
    tempReadings.append(row)
# Second time
for i in range(len(readings)):
    row = []
    for j in range(len(readings[i])):
        if (int(readings[i][j])+2)%9 == 0:
            row.append(9)
        else:
            row.append((int(readings[i][j])+2)%9)
    tempReadings.append(row)
# Third time
for i in range(len(readings)):
    row = []
    for j in range(len(readings[i])):
        if (int(readings[i][j])+3)%9 == 0:
            row.append(9)
        else:
            row.append((int(readings[i][j])+3)%9)
    tempReadings.append(row)
# Forth time
for i in range(len(readings)):
    row = []
    for j in range(len(readings[i])):
        if (int(readings[i][j])+4)%9 == 0:
            row.append(9)
        else:
            row.append((int(readings[i][j])+4)%9)
    tempReadings.append(row)

readings = tempReadings.copy()

# Finding the shortest path
sptSet = [(0,0),]
notSptSet = set()

dataset = [["X" for _ in range(len(readings[0]))] for _ in range(len(readings))]
dataset[0][0] = 0

risk = 0

run = True
while run:
    AddAdj(sptSet[-1], risk)
    minVertex = MinRisk()
    sptSet.append(minVertex)
    risk = dataset[minVertex[0]][minVertex[1]]

    # if the element added to sptSet is the destination then exiting
    if sptSet[-1] == ((len(readings) - 1), (len(readings[-1]) - 1)):
        run = False

print("Part 2")
print("Min Risk with extended map:", risk)