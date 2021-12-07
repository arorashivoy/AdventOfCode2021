# Advent Of coding 
# Day 7
#
# By Shivoy Arora

file = open("input7.txt", "r")

x = [int(i) for i in file.readlines()[0].split(",")]

# Part 1
leastFuel = None

for i in range(max(x)):
    fuel = sum([abs(j - i) for j in x])
    if not leastFuel or fuel < leastFuel:
        leastFuel = fuel

print("Part 1")
print("Least Fuel:", leastFuel)

print()

# Part 2
leastFuel = None

for i in range(max(x)):
    fuel = 0

    for j in x:
        diff = abs(j - i)
        fuel += (diff * (diff + 1)) / 2

    if not leastFuel or fuel < leastFuel:
        leastFuel = fuel

print("Part 2")
print("Least Fuel:", leastFuel)
