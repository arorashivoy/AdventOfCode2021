# Advent Of coding 
# Day 12
#
# By Shivoy Arora

file = open("input/input12.txt", "r")

readings = [i.strip().split("-") for i in file.readlines()]

paths = set()
path = []

connections = dict()

for i in range(len(readings)):
    for j in range(len(readings[i])):
        try:
            _ = connections[readings[i][j]]
            connections[readings[i][j]].add(readings[i][j-1])
        except KeyError:
            connections[readings[i][j]] = set([readings[i][j-1]])

for i in connections["start"]:
    path.append(("start", i))

while path:
    currPath = path.pop()
    for j in connections[currPath[-1]]:
        
        # if small cave is visited
        if j in currPath and j.islower():
            continue

        newPath = currPath + (j,)

        if j == "end" and newPath not in paths:
            paths.add(newPath)
            continue

        if j != "end":
            path.append(newPath)

print("Part 1")
print("Number:", len(paths))

print()

# Part 2 
paths = set()
path = []

for i in connections["start"]:
    path.append((("start", i), False))

while path:
    currPath, revisited = path.pop()
    for j in connections[currPath[-1]]:
        newPathRevisited = revisited
        
        # can't revisit start
        if j == "start":
            continue

        if j in currPath and j.islower():
            if newPathRevisited:
                continue
            else:
                newPathRevisited = True
    
        newPath = currPath + (j,)

        if j == "end" and newPath not in paths:
            paths.add(newPath)
            continue

        if j != "end":
            path.append((newPath, newPathRevisited))

print("Part 2")
print("Number:", len(paths))
