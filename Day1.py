# Advent Of coding 
# Day 1
#
# By Shivoy Arora

file = open("input1.txt", "r")

readings = file.readlines()

# Part 1
ctr1 = 0

for i in range(len(readings) - 1):
    if int(readings[i]) < int(readings[i+1]):
        ctr1 += 1

print("PART 1")
print(ctr1)

print()

# Part 2
ctr2 = 0

for i in range(2, len(readings) - 1):
    if (int(readings[i-2]) + int(readings[i-1]) + int(readings[i])) < (int(readings[i-1]) + int(readings[i]) + int(readings[i+1])):
        ctr2 += 1

print("PART 2")
print(ctr2)
