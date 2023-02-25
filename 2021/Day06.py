# Advent Of coding 
# Day 6
#
# By Shivoy Arora

def sumFind():
    global ages

    ctr = 0

    for i in ages.values():
        ctr += i

    return ctr

file = open("input/input06.txt", "r")

readings = file.readlines()

ages = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for i in readings[0].split(","):
    ages[int(i)] += 1

# Part 1
for _ in range(80):
    new = ages[0]
    ages[0] = ages[1]
    ages[1] = ages[2]
    ages[2] = ages[3]
    ages[3] = ages[4]
    ages[4] = ages[5]
    ages[5] = ages[6]
    ages[6] = ages[7]
    ages[7] = ages[8]

    # For given birth and new born
    ages[8] = new
    ages[6] += new
    

print("Part 1")
print("Count:", sumFind())

print()

# Part 2

# for additional 176 days (total of 256)
for _ in range(176):
    new = ages[0]
    ages[0] = ages[1]
    ages[1] = ages[2]
    ages[2] = ages[3]
    ages[3] = ages[4]
    ages[4] = ages[5]
    ages[5] = ages[6]
    ages[6] = ages[7]
    ages[7] = ages[8]

    # For given birth and new born
    ages[8] = new
    ages[6] += new

print("Part 2")
print("Count:", sumFind())
