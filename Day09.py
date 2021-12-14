# Advent Of coding 
# Day 9
#
# By Shivoy Arora

""" Check Adjacent elements """
def checkAdjacent(i, j, basin: set):
    global readings

    try:
        # if adjacent is X then add to that list
        if readings[i][j+1] == "X":
            for a in range(len(basins)):
                    for b in range(len(basins[a])):
                        if basins[a][b] == (i,j+1):
                            basins[a].extend(basin)
                            basin = set()

                            break
        # if adjacent is not X or 9 then add it to temp list and check its adjacent
        elif readings[i][j+1] != "9":
            readings[i][j+1] = "X"

            basin.add((i, j+1))

            checkAdjacent(i, j+1, basin)
    except IndexError:
        pass
    try:
        if j-1 >= 0:
            # if adjacent is X then add to that list
            if readings[i][j-1] == "X":
                for a in range(len(basins)):
                        for b in range(len(basins[a])):
                            if basins[a][b] == (i,j-1):
                                basins[a].extend(basin)
                                basin = set()

                                break
            # if adjacent is not X or 9 then add it to temp list and check its adjacent
            elif readings[i][j-1] != "9":
                readings[i][j-1] = "X"

                basin.add((i, j-1))

                checkAdjacent(i, j-1, basin)
    except IndexError:
        pass
    try:
        # if adjacent is X then add to that list
        if readings[i+1][j] == "X":
            for a in range(len(basins)):
                    for b in range(len(basins[a])):
                        if basins[a][b] == (i+1,j):
                            basins[a].extend(basin)
                            basin = set()

                            break
        # if adjacent is not X or 9 then add it to temp list and check its adjacent
        elif readings[i+1][j] != "9":
            readings[i+1][j] = "X"

            basin.add((i+1, j))

            checkAdjacent(i+1, j, basin)
    except IndexError:
        pass
    try:
        if i-1 >= 0:
            # if adjacent is X then add to that list
            if readings[i-1][j] == "X":
                for a in range(len(basins)):
                        for b in range(len(basins[a])):
                            if basins[a][b] == (i-1,j):
                                basins[a].extend(basin)
                                basin = set()

                                break
            # if adjacent is not X or 9 then add it to temp list and check its adjacent
            elif readings[i-1][j] != "9":
                readings[i-1][j] = "X"

                basin.add((i-1, j))

                checkAdjacent(i-1, j, basin)
    except IndexError:
        pass

    return basin

""" Main Function """
if __name__ == "__main__":
    file = open("input/input09.txt", "r")
    # file = open("input/test.txt", "r")

    readings = [[j for j in i.strip() ] for i in file.readlines()]

    # Part 1
    lowPoints = []

    # For top edge
    #
    # For leading top corner
    if readings[0][0] < readings[0][1]:
        if readings[0][0] < readings[1][0]:
            lowPoints.append(readings[0][0])

    for j in range(len(readings[0]) - 1):
        if readings[0][j] < readings[0][j-1] and readings[0][j] < readings[0][j+1]:
            if readings[0][j] < readings[1][j]:
                lowPoints.append(readings[0][j])

    # For trailing top corner
    if readings[0][-1] < readings[0][-2]:
        if readings[0][-1] < readings[1][-1]:
            lowPoints.append(readings[0][-1])

    # For middle rows
    for i in range(1, len(readings) - 1):

        # for leading edge
        if readings[i][0] < readings[i][1]:
            if readings[i][0] < readings[i+1][0] and readings[i][0] < readings[i-1][0]:
                lowPoints.append(readings[i][0])

        for j in range(1, len(readings[i]) - 1):

            if readings[i][j] < readings[i][j-1] and readings[i][j] < readings[i][j+1]:
                if readings[i][j] < readings[i-1][j] and readings[i][j] < readings[i+1][j]:
                    lowPoints.append(readings[i][j])

        # For trailing edge
        if readings[i][-1] < readings[i][-2]:
            if readings[i][-1] < readings[i+1][-1] and readings[i][-1] < readings[i-1][-1]:
                lowPoints.append(readings[i][-1])

    # For bottom edge
    #
    # For leading bottom corner
    if readings[-1][0] < readings[-1][1]:
        if readings[-1][0] < readings[-2][0]:
            lowPoints.append(readings[0][0])

    for j in range(len(readings[-1]) - 1):
        if readings[-1][j] < readings[-1][j-1] and readings[-1][j] < readings[-1][j+1]:
            if readings[-1][j] < readings[-2][j]:
                lowPoints.append(readings[-1][j])

    # For trailing bottom corner
    if readings[-1][-1] < readings[-1][-2]:
        if readings[-1][-1] < readings[-2][-1]:
            lowPoints.append(readings[-1][-1])

    print("Part 1")
    print("Sum of risk:", sum([int(i) for i in lowPoints]) + len(lowPoints) )

    print()

    # Part 2
    """
    List of all the basins
    element :- list of coordinates of the all point in that basin
    """
    basins = []

    for i in range(len(readings)):
        for j in range(len(readings[i])):

            if readings[i][j] != "9" and readings[i][j] != "X":
                readings[i][j] = "X"

                basin = checkAdjacent(i, j, set([(i,j),]))
                if basin != set():
                    basins.append(list(basin))

    basinLen = sorted([len(i) for i in basins], reverse=True)

    print("Part 2")
    print("Largest elements: {}, {}, {}".format(basinLen[0], basinLen[1], basinLen[2]))
    print("Product", basinLen[0] * basinLen[1] * basinLen[2])
