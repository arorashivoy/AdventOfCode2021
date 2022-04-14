# Advent Of coding
# Day 23
#
# By Shivoy Arora

from re import L


file = open("input/input23.txt", "r")

readings = file.readlines()
file.close()

columns = [[i] for i in readings[3].strip().strip("#").split("#")]

l = readings[2].strip().strip("#").split("#")
for i in range(4):
    columns[i].append(l[i])

del l
