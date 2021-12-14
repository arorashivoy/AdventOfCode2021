# Advent Of coding 
# Day 9 
# Visualisation
#
# By Shivoy Arora

import pygame

""" Pygame show all readings """
def show(readings):
    global side
    global basins

    for i in range(len(readings)):
        for j in range(len(readings[i])):
            if readings[i][j] == "9":
                pygame.draw.rect(win, (136,149,179), (x+side*j, y+side*i, side, side))
            elif readings[i][j] == "X":
                pygame.draw.rect(win, (187,173,255), (x+side*j, y+side*i, side, side))
            else:
                pygame.draw.rect(win, (142,148,242), (x+side*j, y+side*i, side, side))
    
    # mark each point
    numBasins = font.render("Basins: {}".format(len(basins)), True, (165,161,249))
    # Show basins number
    win.blit(numBasins, (25, 550))

""" Check Adjacent elements """
def checkAdjacent(i, j, basin: set):
    global readings

    pygame.time.delay(50)

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

            win.fill((0,0,0))
            show(readings)
            pygame.display.update()

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

                win.fill((0,0,0))
                show(readings)
                pygame.display.update()

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

            win.fill((0,0,0))
            show(readings)
            pygame.display.update()

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

                                break
            # if adjacent is not X or 9 then add it to temp list and check its adjacent
            elif readings[i-1][j] != "9":
                readings[i-1][j] = "X"

                win.fill((0,0,0))
                show(readings)
                pygame.display.update()

                basin.add((i-1, j))

                checkAdjacent(i-1, j, basin)
    except IndexError:
        pass

    return basin

""" Main Function """
if __name__ == "__main__":
    # Pygame setup
    pygame.init()

    win = pygame.display.set_mode((550,600))
    pygame.display.set_caption("Day 9 Basins")
    font = pygame.font.SysFont(None, 30)

    x = 25
    y = 25

    side = 5

    # Solving
    file = open("input/input09.txt","r")
    readings = [[j for j in i.strip() ] for i in file.readlines()]

    """
    List of all the basins
    element :- list of coordinates of the all point in that basin
    """
    basins = []

    # initialising when nothing is pressed 
    win.fill((0,0,0))
    show(readings)
    pygame.display.update()

    execute = False
    run = True
    index = 0
    rowIndex = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    execute = not execute
                elif event.key == pygame.K_o:
                    basinLen = sorted([len(i) for i in basins], reverse=True)

                    print()

                    print("Largest basins: {}, {}, {}".format(basinLen[0], basinLen[1], basinLen[2]))
                    print("Product", basinLen[0] * basinLen[1] * basinLen[2])

        if execute:
            if readings[index][rowIndex] != "9" and readings[index][rowIndex] != "X":
                readings[index][rowIndex] = "X"

                win.fill((0,0,0))
                show(readings)
                pygame.display.update()

                basin = checkAdjacent(index, rowIndex, set([(index,rowIndex),]))
                if basin != set():
                    basins.append(list(basin))
            
            rowIndex += 1
            if index < len(readings) - 1 and rowIndex == len(readings[index]):
                index += 1
                rowIndex = 0
            elif index == len(readings) - 1:
                execute = False
                run = False
        else:
            win.fill((0,0,0))
            show(readings)
            pygame.draw.polygon(win, (255,0,0), [(525,557.5), (503.5,545),(503.5,570)])
            pygame.display.update()
            win.fill((0,0,0))
