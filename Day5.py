# Advent Of coding 
# Day 5
#
# By Shivoy Arora

""" To draw horzinal and vertical lines in the coordinate system """
def drawInCoord(x1, y1, x2, y2, Coordinates):
    if y1 == y2:
        if x1 < x2: 
            for i in range(x1, x2 + 1):
                Coordinates[y1][i] += 1
        else:
            for i in range(x2, x1 + 1):
                Coordinates[y1][i] += 1

    elif x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                Coordinates[i][x1] += 1
        else:
            for i in range(y2, y1 + 1):
                Coordinates[i][x1] += 1

    elif (y2 - y1)/(x2 - x1) == 1:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                Coordinates[i - x1 + y1][i] += 1
        else:
            for i in range(x2, x1 + 1):
                Coordinates[i - x1 + y1][i] += 1

    elif (y2 - y1)/(x2 - x1) == -1:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                Coordinates[-i + x1 + y1][i] += 1
        else:
            for i in range(x2, x1 + 1):
                Coordinates[-i + x1 + y1][i] += 1

""" Count the number of points where lines overlap """
def countOverlap(Coordinates):
    ctr = 0

    for i in Coordinates:
        for j in i:
            if j > 1:
                ctr += 1

    return ctr

""" Main Function """
if __name__ == "__main__":
    file = open("input/input5.txt", "r")

    readings = file.readlines()

    # Part 1
    #
    # Setting up coordinate system in an array
    Coordinates1 = [
        [0 for _ in range(1000)] for _ in range(1000)
    ]

    # Part 2
    #
    # Setting up coordinate system in an array
    Coordinates2 = [
        [0 for _ in range(1000)] for _ in range(1000)
    ]

    for i in readings:
        line = i.strip().split("->")

        x1 = int(line[0].split(",")[0].strip())
        y1 = int(line[0].split(",")[1].strip())

        x2 = int(line[1].split(",")[0].strip())
        y2 = int(line[1].split(",")[1].strip())

        # Part 1
        if x1 == x2 or y1 == y2:
            drawInCoord(x1, y1, x2, y2, Coordinates1)
        
        # Part 2
        drawInCoord(x1, y1, x2, y2, Coordinates2)

    print("Part 1")
    print("Points:", countOverlap(Coordinates1))

    print()

    print("Part 2")
    print("Points:", countOverlap(Coordinates2))
    