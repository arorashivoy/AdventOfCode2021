# Advent Of coding 
# Day 11 
# Visualization
#
# By Shivoy Arora

import pygame
from pygame import font

""" Increasing the energy of the adjacent octopus """
def incAdjEnergy(i, j):
    global readings

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


def show(readings, execute):
    for i in range(len(readings)):
        for j in range(len(readings[i])):
            if readings[i][j] == 0:
                pygame.draw.rect(win, (30, 200, 255) if execute else (255,255,0), (x + 20*j, y + 20*i, width, width))
            else:
                pygame.draw.rect(win, (0,0,0), (x + 20*j, y + 20*i, width, width))

if __name__ == "__main__":

    # Setting up pygame
    pygame.init()

    win = pygame.display.set_mode((250,300))
    pygame.display.set_caption("Day 11 flashes")
    font = pygame.font.SysFont(None, 30)

    x = 25
    y = 25

    width = 20

    # Solving
    file = open("input/input11.txt", "r")
    readings = [[int(j) for j in i.strip()]for i in file.readlines()]

    syncedReadings = [[0 for _ in range(10)] for _ in range(10)]

    run = True

    flashed = 0

    # initial when nothing is pressed
    win.fill((0,0,0))

    show(syncedReadings, False)
    pygame.display.update()

    flashes = 0
    execute = False
    while run:

        steps = font.render("Steps: {}".format(flashes), True, (30,200,255) if execute else (255,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    execute = not execute

        if not execute:
            win.fill((0,0,0))
            show(readings, execute)
            win.blit(steps, (25, 250))
            pygame.display.update()

        else:
            flashes += 1

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

            win.fill((0,0,0))

            show(readings, execute)
            win.blit(steps, (25, 250))
            pygame.display.update()

            pygame.time.delay(50)
            
            if readings == syncedReadings:
                flashed += 1

            if flashed == 5:
                run = False
    
    pygame.quit()
