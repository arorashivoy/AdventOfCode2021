# Advent Of coding 
# Day 25
#
# By Shivoy Arora

file = open("input/input25.txt", "r")

readings = [[j for j in i.strip()] for i in file.readlines()]

# for i in readings:
#     for j in i:
#         print(j,end="")
#     print()

ctr = 0
changesMade = True
while changesMade:
    changesMade = False

    # Going east
    alreadyMoved = []
    for i in range(len(readings)):
        for j in range(len(readings[i])):
            if readings[i][j] == ">":
                if (i,j) not in alreadyMoved:
                    if j < len(readings[i]) - 1:
                        if readings[i][j+1] == ".":
                            readings[i][j+1], readings[i][j] = ">", "."
                            alreadyMoved.append((i,j+1))

                            changesMade = True
                    else:
                        if readings[i][0] == "." and (i, 1) not in alreadyMoved:
                            readings[i][0], readings[i][j] = ">", "."
                            alreadyMoved.append((i,0))

                            changesMade = True

    # Going south
    alreadyMoved = []
    for i in range(len(readings)):
        for j in range(len(readings[i])):
            if readings[i][j] == "v":
                if (i,j) not in alreadyMoved:
                    if i < len(readings) - 1:
                        if readings[i+1][j] == ".":
                            readings[i+1][j], readings[i][j] = "v", "."
                            alreadyMoved.append((i+1,j))

                            changesMade = True
                    else:
                        if readings[0][j] == "." and (1, j) not in alreadyMoved:
                            readings[0][j], readings[i][j] = "v", "."
                            alreadyMoved.append((0,j))

                            changesMade = True

    ctr += 1
    if not changesMade:
        break


print("Step", ctr)
# for i in readings:
#     for j in i:
#         print(j,end="")
#     print()
