# Advent Of coding 
# Day 18
#
# By Shivoy Arora

""" To reduce shell number """
def reduceNum(shellNums):
    # Adding for the first two equations
    ans = "[{},{}]".format(shellNums[0], shellNums[1])
    ansList = [a for a in ans if a != " "]

    # adding the numbers and reducing
    while True:
        # reducing ans
        i = 0
        while i < len(ansList):
            try:
                num = int(ansList[i])

                pairs = 0
                for j in range(i, -1, -1):
                    if ansList[j] == "[":
                        pairs += 1
                    elif ansList[j] == "]":
                        pairs -= 1

                # pair nested under 4 pairs
                if pairs > 4:
                    # adding first num to prev num
                    for j in range(i-1, -1, -1):
                        try:
                            prevNum = int(ansList[j])
                            prevNum += num

                            ansList[j] = "{}".format(prevNum)
                            break
                        except ValueError:
                            pass
                    
                    # adding second num to next num
                    pairNum = None
                    for j in range(i+1, len(ansList)):
                        try:
                            if not pairNum and pairNum != 0:
                                pairNum = int(ansList[j])
                                continue
                            nextNum = int(ansList[j])
                            nextNum += pairNum

                            ansList[j] = "{}".format(nextNum)
                            break
                            
                        except ValueError:
                            pass

                    # removing pair
                    for _ in range(5):
                        ansList.pop(i-1)

                    # Adding 0 in place of pair
                    ansList.insert(i-1, "0")

                    i = 0
                    continue
            
            except ValueError:
                pass

            i += 1

        # if num is greater than 9
        try:
            i = 0
            while i < len(ansList):
                try:
                    num = int(ansList[i])
                except ValueError:
                    i += 1
                    continue
                    
                if num > 9:
                    ansList.pop(i)

                    ansList.insert(i, "]")
                    ansList.insert(i, "{}".format((num//2) + (num%2)))
                    ansList.insert(i, ",")
                    ansList.insert(i, "{}".format(num//2))
                    ansList.insert(i, "[")

                    i = 0
                    raise AssertionError("A number has been split")

                i += 1

        # if a number is split then go to the start to check if explode is required
        except AssertionError:
            continue

        for _ in range(2):
            shellNums.pop(0)

        ans = "".join(ansList)
        shellNums.insert(0, ans)

        if len(shellNums) != 1:
            ans = "[{},{}]".format(shellNums[0], shellNums[1])
            ansList = [a for a in ans if a != " "]
        else:
            break

    return ansList

""" To find the magnitude of shell number """
def Mag(ansList):
    i = 0
    while i < len(ansList):
        try:
            num = int(ansList[i])
            
            # if it doesn't have any sub pairs
            if ansList[i-1] == "[" and ansList[i+3] == "]":
                num2 = int(ansList[i+2])
                mag = (3*num) + (2*num2)

                # removing pair
                for _ in range(5):
                    ansList.pop(i-1)

                ansList.insert(i-1, "{}".format(mag))

                i = 0
                continue

        except ValueError:
            pass

        i += 1
    
    return int(ansList[0])

if __name__ == "__main__":
    file = open("input/input18.txt", "r")
    readings = [i.strip() for i in file.readlines()]

    # Part 1
    ansList = reduceNum(readings.copy())

    print("Part 1")
    print("Magnitude:", Mag(ansList))

    print()

    # Part 2
    maxMag = None
    for i in readings:
        for j in readings:
            if i != j:
                ansList = reduceNum([i,j])

                mag = Mag(ansList)

                if not maxMag:
                    maxMag = mag
                elif maxMag < mag:
                    maxMag = mag

    print("Part 2")
    print("Max magnitude:", maxMag)
