# Advent Of coding 
# Day 22
#
# By Shivoy Arora

""" Check if the region intersect with already created regions and remove overlap """
def IntersectingCubes(minX, maxX, minY, maxY, minZ, maxZ):
    global cubeRanges
    
    i = 0
    while i < len(cubeRanges):
        try: 
            if maxX > min(cubeRanges[i][0]) and max(cubeRanges[i][0]) > minX and maxZ > min(cubeRanges[i][2]) and max(cubeRanges[i][2]) > minZ and maxY > min(cubeRanges[i][1]) and max(cubeRanges[i][1]) > minY:
                # # Top half 
                # cubeRanges.append((cubeRanges[i][0], cubeRanges[i][1], range(min(cubeRanges[i][2]), minZ+1)))
                # # Bottom half
                # cubeRanges.append((cubeRanges[i][0], cubeRanges[i][1], range(maxZ, max(cubeRanges[i][2])+1)))
                # # left
                # cubeRanges.append((range(min(cubeRanges[i][0]), minX+1), cubeRanges[i][1], range(minZ, maxZ+1)))
                # # right
                # cubeRanges.append((range(maxX, max(cubeRanges[i][0])+1), cubeRanges[i][1], range(minZ, maxZ+1)))
                # # front
                # cubeRanges.append((range(minX, maxX+1), range(maxY, max(cubeRanges[i][1])+1), range(minZ, maxZ+1)))
                # # back
                # cubeRanges.append((range(minX, maxX+1), range(min(cubeRanges[i][1]), minY+1), range(minZ, maxZ+1)))

                cubeRanges.pop(i)

                i = 0
                continue
        except ValueError:
            pass

        i += 1


""" Main Function """
file = open("input/input22.txt","r")
readings = [[i.strip().split()[0], [tuple([int(j[2:].split("..")[0]),int(j[2:].split("..")[1])]) for j in i.strip().split()[1].split(",")]] for i in file.readlines()]

# Part 1
onCubes = set()

for i in range(len(readings)):
    try:
        if readings[i][1][0][0] <= 50 and readings[i][1][0][1] >= -50:
            minX = readings[i][1][0][0] if readings[i][1][0][0] in range(-50,51) else -50
            maxX = readings[i][1][0][1] if readings[i][1][0][1] in range(-50,51) else 50
        else:
            raise AssertionError("Range out of initialization")

        if readings[i][1][1][0] <= 50 and readings[i][1][1][1] >= -50:
            minY = readings[i][1][1][0] if readings[i][1][1][0] in range(-50,51) else -50
            maxY = readings[i][1][1][1] if readings[i][1][1][1] in range(-50,51) else 50
        else:
            raise AssertionError("Range out of initialization")

        if readings[i][1][2][0] <= 50 and readings[i][1][2][1] >= -50:
            minZ = readings[i][1][2][0] if readings[i][1][2][0] in range(-50,51) else -50
            maxZ = readings[i][1][2][1] if readings[i][1][2][1] in range(-50,51) else 50
        else:
            raise AssertionError("Range out of initialization")

        for x in range(minX, maxX+1):
            for y in range(minY, maxY+1):
                for z in range(minZ, maxZ+1):
                    if readings[i][0] == "on":
                        onCubes.add(tuple([x,y,z]))

                    elif readings[i][0] == "off":
                        onCubes.discard(tuple([x,y,z]))

    except AssertionError:
        continue

print("Part 1")
print("No of on Cubes:", len(onCubes))

print()

# Part 2
cubeRanges = []

for i in range(len(readings)):

    minX = readings[i][1][0][0]
    maxX = readings[i][1][0][1]

    minY = readings[i][1][1][0]
    maxY = readings[i][1][1][1]

    minZ = readings[i][1][2][0]
    maxZ = readings[i][1][2][1]

    if readings[i][0] == "on":
        IntersectingCubes(minX,maxX,minY,maxY,minZ,maxZ)
        cubeRanges.append((range(minX, maxX+1), range(minY, maxY+1), range(minZ, maxZ+1)))

    elif readings[i][0] == "off":
        IntersectingCubes(minX,maxX,minY,maxY,minZ,maxZ)

print("len", len(cubeRanges))
# Finding the num of cubes on
cubesOn = 0
for i in cubeRanges:
    try:
        cubesOn += (max(i[0])-min(i[0])+1)*(max(i[1])-min(i[1])+1)*(max(i[2])-min(i[2])+1)
    except ValueError:
        continue

print(cubesOn)
