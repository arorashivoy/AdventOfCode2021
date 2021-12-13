# Advent Of coding 
# Day 8
#
# By Shivoy Arora

file = open("input/input8.txt", "r")

readings = file.readlines()

connections = [i.strip().split("|")[0].split() for i in readings]
output = [i.strip().split("|")[1].split() for i in readings]

# Part 1
uniqueCtr = 0

for i in output:
    for j in i:
        if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
            uniqueCtr += 1

print("Part 1")
print("Unique Count:", uniqueCtr)

print()

# Part 2
outputSum = 0

for i in range(len(connections)):
    """ Making out the connections """
    # lists of numbers with the respective no. of letters
    ch2 = []
    ch3 = []
    ch4 = []
    ch5 = []
    ch6 = []

    """
    Arrangements of the segments

     666
    5   1
     777 
    4   2
     333

    """

    # sets of the possible outcomes of segments
    segAll = {"a","b","c","d","e","f","g"}
    seg1 = set()
    seg2 = set()
    seg3 = set()
    seg4 = set()
    seg5 = set()
    seg6 = set()
    seg7 = set()

    for j in connections[i]:
        if len(j) == 2:
            ch2 = [a for a in j]
        elif len(j) == 4:
            ch4 = [a for a in j]
        elif len(j) == 3:
            ch3 = [a for a in j]
        elif len(j) == 5:
            ch5.append(j)
        elif len(j) == 6:
            ch6.append(j)

    # using 1
    seg1 = {ch2[0], ch2[1]}
    # using 7
    seg6 = {i for i in ch3 if i not in seg1}
    # using 4
    seg5 = {i for i in ch4 if i not in seg1}
    # using 9
    seg3 = {j for i in ch6 if set.union(seg1,seg6,seg5).issubset(i) for j in i} - set.union(seg1,seg6,seg5)
    # eliminating 9 from all segments
    seg4 = segAll - set.union(seg1,seg6,seg5,seg3)
    # using 3
    seg7 = {j for i in ch5 if set.union(seg1, seg3, seg6).issubset(i) for j in i if j not in set.union(seg1, seg3, seg6)}
    # seg5 and seg7 were entangled
    seg5 = seg5 - seg7
    # using 5
    seg2 = {j for i in ch6 if set.union(seg3, seg4, seg5, seg6, seg7).issubset(i) for j in i} - set.union(seg3, seg4, seg5, seg6, seg7)
    # seg1 and seg2 are entangled
    seg1 = seg1 - seg2

    """Finding the output numbers"""
    num = 0

    for j in output[i]:
        segs = {i for i in j}
        # Number 1
        if segs == set.union(seg1, seg2):
            num = (num * 10) + 1
        # Number 2
        elif segs == set.union(seg6, seg1, seg7, seg4, seg3):
            num = (num * 10) + 2
        # Number 3
        elif segs == set.union(seg6,seg1,seg7,seg2,seg3):
            num = (num * 10) + 3
        # Number 4
        elif segs == set.union(seg5,seg7,seg1,seg2):
            num = (num * 10) + 4
        # Number 5
        elif segs == set.union(seg6,seg5,seg7,seg2,seg3):
            num = (num * 10) + 5
        # Number 6
        elif segs == set.union(seg6,seg5,seg7,seg2,seg3,seg4):
            num = (num * 10) + 6
        # Number 7
        elif segs == set.union(seg6,seg1,seg2):
            num = (num * 10) + 7
        # Number 8
        elif segs == segAll:
            num = (num * 10) + 8
        # Number 9
        elif segs == set.union(seg7,seg5,seg6,seg1,seg2,seg3):
            num = (num * 10) + 9
        # Number 0
        elif segs == set.union(seg1,seg2,seg3,seg4,seg5,seg6):
            num = num * 10

    outputSum += num

print("Part 2")
print("Sum:",outputSum)
