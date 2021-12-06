# Advent Of coding 
# Day 2
#
# By Shivoy Arora

file = open("input2.txt", "r")

readings = file.readlines()

# Part 1
x = 0
y = 0

for i in readings:
    j = i.split()

    if j[0].strip() == "forward":
        x += int(j[1])
    elif j[0].strip() == "down":
        y += int(j[1])
    elif j[0].strip() == "up":
        y -= int(j[1])

print("PART 1")
print("x: {}\ny: {}".format(x,y))
print("\nProduct: {}".format(x * y))

print()

# Part 2

aim = 0
x = 0
y = 0

for i in readings:
    j = i.split()

    if j[0].strip() == "forward":
        x += int(j[1])
        y += int(j[1]) * aim
    elif j[0].strip() == "down":
        aim += int(j[1])
    elif j[0].strip() == "up":
        aim -= int(j[1])

print("PART 2")
print("x: {}\ny: {}\naim: {}".format(x, y, aim))
print("\nProduct: {}".format(x * y))
