# Advent Of coding 
# Day 11
#
# By Shivoy Arora

""" Increasing the energy of the adjacent octopus """
def incAdjEnergy(i, j):
    # Increasing energy of adjacent octo
    try:
        if i > 0:
            readings[i-1][j] += 1
            if readings[i-1][j] == 10:
                incAdjEnergy(i-1, j)
    except IndexError:
        pass
    try:
        readings[i+1][j] += 1
        if readings[i+1][j] == 10:
            incAdjEnergy(i+1, j)
    except IndexError:
        pass
    try:
        if j > 0:
            readings[i][j-1] += 1
            if readings[i][j-1] == 10:
                incAdjEnergy(i, j-1)
    except IndexError:
        pass
    try:
        readings[i][j+1] += 1
        if readings[i][j+1] == 10:
            incAdjEnergy(i,j+1)
    except IndexError:
        pass
    try:
        if i > 0 and j > 0:
            readings[i-1][j-1] += 1
            if readings[i-1][j-1] == 10:
                incAdjEnergy(i-1,j-1)
    except IndexError:
        pass
    try:
        if i > 0:
            readings[i-1][j+1] += 1
            if readings[i-1][j+1] == 10:
                incAdjEnergy(i-1, j+1)
    except IndexError:
        pass
    try:
        readings[i+1][j+1] += 1
        if readings[i+1][j+1] == 10:
            incAdjEnergy(i+1, j+1)
    except IndexError:
        pass
    try:
        if j > 0:
            readings[i+1][j-1] += 1
            if readings[i+1][j-1] == 10:
                incAdjEnergy(i+1, j-1)
    except IndexError:
        pass


""" Main Function """
if __name__ == "__main__":
    file = open("input/input11.txt", "r")

    readings = [[int(j) for j in i.strip()]for i in file.readlines()]

    flashes = 0

    flashed = 0
    synced = False

    syncedReadings = [[0 for _ in range(10)] for _ in range(10)]

    while not synced:
        flashed += 1

        # increasing energy
        for i in range(len(readings)):
            for j in range(len(readings[i])):
                readings[i][j] += 1

                if readings[i][j] == 10:
                    incAdjEnergy(i,j)

        # Flashing if energy greater than 9
        for i in range(len(readings)):
            for j in range(len(readings[i])):
                if readings[i][j] > 9:
                    readings[i][j] = 0
                    flashes += 1

        if flashed == 100:
            # Part 1

            print("Part 1")
            print("Flashes:",flashes)

            print()

        # Part 2
        if readings == syncedReadings:
            synced = True

    print("Part 2")
    print("Synced after:", flashed)
