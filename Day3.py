# Advent Of coding 
# Day 3
#
# By Shivoy Arora

from os import read


file = open("input3.txt", "r")

readings = file.readlines()

# Part 1
gamma = ""
epsilon = ""

for j in range(len(readings[0].strip())):
    ctr0 = 0
    ctr1 = 0

    for i in readings:
        if i.strip()[j] == "0":
            ctr0 += 1
        elif i.strip()[j] == "1":
            ctr1 += 1
    if ctr0 > ctr1:
        gamma += "0"
        epsilon += "1"
    elif ctr0 < ctr1:
        gamma += "1"
        epsilon += "0"    

print("PART 1")
print("Binary")
print("Gamma: {}\nEpsilon: {}".format(gamma, epsilon))

print()

gammaDecimal = 0
epsilonDecimal = 0

for i in range(len(gamma)):
    gammaDecimal += int(gamma[len(gamma) - i - 1]) * (2**i)
    epsilonDecimal += int(epsilon[len(epsilon) - i - 1]) * (2**i)

print("Decimal")
print("Gamma: {}\nEpsilon: {}".format(gammaDecimal, epsilonDecimal))
print("Product:",gammaDecimal * epsilonDecimal)

print()

# Part 2

oCriteria = readings
cCriteria = readings

for j in range(len(readings[0].strip())):

    # For oxygen generator rating
    ctr0 = 0
    ctr1 = 0

    for i in oCriteria:
        if i.strip()[j] == "0":
            ctr0 += 1
        elif i.strip()[j] == "1":
            ctr1 += 1

    if ctr0 > ctr1 :
        oCriteria = [item for item in oCriteria if item.strip()[j] == "0"]
    else:
        oCriteria = [item for item in oCriteria if item.strip()[j] == "1"]

    # For co2 scruber rating
    ctr0 = 0
    ctr1 = 0

    if len(cCriteria) > 1:
        for i in cCriteria:
            if i.strip()[j] == "0":
                ctr0 += 1
            elif i.strip()[j] == "1":
                ctr1 += 1

        if ctr1 < ctr0 :
            cCriteria = [item for item in cCriteria if item.strip()[j] == "1"]
        else:
            cCriteria = [item for item in cCriteria if item.strip()[j] == "0"]

oCriteria = oCriteria[0].strip()
cCriteria = cCriteria[0].strip()

print("Part 2")
print("Binary")
print("Oxygen: {}\nCO2: {}".format(oCriteria, cCriteria))

oDecimal = 0
cDecimal = 0

for i in range(len(oCriteria)):
    oDecimal += int(oCriteria[len(oCriteria) - i - 1]) * (2**i)
    cDecimal += int(cCriteria[len(cCriteria) - i - 1]) * (2**i)

print("\nDecimal")
print("Oxygen: {}\nCO2: {}".format(oDecimal, cDecimal))
print("Product:", oDecimal * cDecimal)
