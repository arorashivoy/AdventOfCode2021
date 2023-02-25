# Advent Of coding 
# Day 10
#
# By Shivoy Arora

def findError(readings):
    global corruptedLines
    global incompChunks

    for i in range(len(readings)):
        rowEleIndex = set() # Rename

        for j in range(len(readings[i])):
            if readings[i][j] in starts:
                bracIndex = starts.index(readings[i][j])

                loopStart = j   # Rename
                subChunkStart = []  # Rename
                for k in range(j, len(readings[i])):
                    
                    if readings[i][k] == ends[bracIndex]:
                        # checking if it is ending of another subchunk of same type
                        for l in range(k, loopStart, -1):
                            if readings[i][l] == starts[bracIndex] and l not in subChunkStart:
                                subChunkStart.append(l)

                                # If there is a sub chunk is of the same type
                                break
                        else:

                            # When this chunk has ended
                            break
                else:
                    if k == len(readings[i]) - 1:
                        k = -1
                
                # print(i,j,k)

                # If number of open brac and close brack not same in the chunk 
                # Then row is corrupted
                if k != -1:
                    chunkStarts = 0
                    chunkEnds = 0

                    for a in range(j+1,k):
                        if readings[i][a] in starts:
                            chunkStarts += 1
                        elif readings[i][a] in ends:
                            chunkEnds += 1
                    
                    if chunkStarts != chunkEnds:
                        corruptedLines.setdefault(i,k)

                elif k == -1:
                    try:
                        _ = incompChunks[i]
                        incompChunks[i].append(j)
                    except KeyError:
                        incompChunks[i] = [j]


                rowEleIndex.add(j)
                rowEleIndex.add(k)
        
        # When this row is complete check whether all the elements exists 
        # If yes then the row is not corrupted
        if rowEleIndex != set([a for a in range(len(readings[i]))] + [-1]):
            corruptedLines.setdefault(i,k)


""" Main Function """
file = open("input/input10.txt", "r")

readings = [[j for j in i.strip()] for i in file.readlines()]

starts = ("[","(","{","<")
ends = ("]",")","}",">")

# Part 1
corruptedLines = dict()

incompChunks = dict()

findError(readings)

errorScore = 0

for (i, k) in corruptedLines.items():
    if readings[i][k] == ")":
        errorScore += 3
    elif readings[i][k] == "]":
        errorScore += 57
    elif readings[i][k] == "}":
        errorScore += 1197
    elif readings[i][k] == ">":
        errorScore += 25137

print("Part 1")
print("Error Score:", errorScore)

print()

# Part 2
lines = [readings[i] for i in range(len(readings)) if i not in corruptedLines.keys()]

incompChunks = dict()

findError(lines)

scores = []

for i in incompChunks:
    score = 0

    a = sorted(incompChunks[i], reverse=True)

    for j in a:
        if lines[i][j] == "(":
            score = (score * 5) + 1
        elif lines[i][j] == "[":
            score = (score * 5) + 2
        elif lines[i][j] == "{":
            score = (score * 5) + 3
        elif lines[i][j] == "<":
            score = (score * 5) + 4

    scores.append(score)

scores.sort()

print("Middle Score:", scores[len(scores)//2])
