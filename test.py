# Day 9
#
# https://github.com/IanFindlay/advent-of-code/blob/master/2021/

def checkAdjacent(i, j, basin: set):
    global readings

    try:
        # if adjacen tis X then add to that list
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
            # if adjacen tis X then add to that list
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
        # if adjacen tis X then add to that list
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
            # if adjacen tis X then add to that list
            if readings[i-1][j] == "X":
                for a in range(len(basins)):
                        for b in range(len(basins[a])):
                            if basins[a][b] == (i-1,j):
                                basins[a].extend(basin)
                                basin = set()
                                added = True

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
    
    file = open("input/input9.txt", "r")

    readings = [[j for j in i.strip() ] for i in file.readlines()]

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
