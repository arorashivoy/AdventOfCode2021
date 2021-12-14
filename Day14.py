# Advent Of coding 
# Day 14
#
# By Shivoy Arora

file = open("input/input14.txt","r")

template = file.readline().strip()

rules = [[j.strip() for j in i.split("->")] for i in file.readlines() if i.strip() != ""]

pairs = dict()
for i in range(len(template)):
    if template[i:i+2] in pairs:
        pairs[template[i:i+2]] += 1
    else:
        pairs[template[i:i+2]] = 1

# Part 1
for _ in range(10):
    newPairs = dict()
    for i, num in pairs.items():
        for j in rules:
            if j[0] == i:
                if i[0]+j[1] in newPairs:
                    newPairs[i[0]+j[1]] += num
                else:
                    newPairs[i[0]+j[1]] = num

                if j[1]+i[1] in newPairs:
                    newPairs[j[1]+i[1]] += num
                else:
                    newPairs[j[1]+i[1]] = num

    pairs = newPairs

allFreq = dict()
for i, num in pairs.items():
    if i[0] in allFreq:
        allFreq[i[0]] += num
    else:
        allFreq[i[0]] = num

allFreq[template[-1]] += 1

print("Part 1")
print("Max: {}, Min: {}".format(max(allFreq.values()), min(allFreq.values())))
print("Difference:", max(allFreq.values()) - min(allFreq.values()))

print()

# Part 2
for _ in range(30):
    newPairs = dict()
    for i, num in pairs.items():
        for j in rules:
            if j[0] == i:
                if i[0]+j[1] in newPairs:
                    newPairs[i[0]+j[1]] += num
                else:
                    newPairs[i[0]+j[1]] = num

                if j[1]+i[1] in newPairs:
                    newPairs[j[1]+i[1]] += num
                else:
                    newPairs[j[1]+i[1]] = num

    pairs = newPairs

allFreq = dict()
for i, num in pairs.items():
    if i[0] in allFreq:
        allFreq[i[0]] += num
    else:
        allFreq[i[0]] = num

allFreq[template[-1]] += 1

print("Part 2")
print("Max: {}, Min: {}".format(max(allFreq.values()), min(allFreq.values())))
print("Difference:", max(allFreq.values()) - min(allFreq.values()))
