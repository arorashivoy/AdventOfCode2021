# Advent Of coding 
# Day 25
#
# By Shivoy Arora

import pygame

def show(readings):
    global width, x, y
    global steps

    win.fill((0,0,0))
    for i in range(len(readings)):
        for j in range(len(readings[i])):
            if readings[i][j] == "v":
                pygame.draw.rect(win, "#EE6C4D", (x+width*j, y+width*i, width, width))
            elif readings[i][j] == ">":
                pygame.draw.rect(win, "#98C1D9", (x+width*j, y+width*i, width, width))

    numStep = font.render("Steps: {}".format(steps), True, "#E0FBFC")
    win.blit(numStep, (25, 590))

""" Main Function """
if __name__ == "__main__":
    # Pygame setup
    pygame.init()

    win = pygame.display.set_mode((600,650))
    pygame.display.set_caption("Day 25 Sea Cucumber")
    font = pygame.font.SysFont(None, 30)

    x = 25
    y = 25

    width = 4

    # Solving
    file = open("input/input25.txt", "r")
    readings = [[j for j in i.strip()] for i in file.readlines()]

    steps = 0

    run = True
    execute = False
    while run:

        # For keypress and quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    execute = not execute
                elif event.key == pygame.K_q:
                    execute = False
                    run = False

        # executing the solution
        if execute:
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

            # Show result 
            show(readings)
            pygame.display.update()

            steps += 1
            if not changesMade:
                execute = False

        # If program is paused
        else:
            win.fill((0,0,0))
            show(readings)
            pygame.draw.polygon(win, (255,0,0), [(575,607.5), (553.5,595),(553.5,620)])
            pygame.display.update()
