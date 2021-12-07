# Advent Of coding 
# Day 4
#
# By Shivoy Arora


""" For marking the chosen number """
def markChosen(boardIndex: int):
    global chosenNumbers
    global finalBoards
    global won
    global row0, row1, row2, row3, row4

    won = False
    
    for j in range(len(chosenNumbers)):
        if not won:
            if chosenNumbers[j] in row0:
                row0[row0.index(chosenNumbers[j])] = "X"
            elif chosenNumbers[j] in row1:
                row1[row1.index(chosenNumbers[j])] = "X"
            elif chosenNumbers[j] in row2:
                row2[row2.index(chosenNumbers[j])] = "X"
            elif chosenNumbers[j] in row3:
                row3[row3.index(chosenNumbers[j])] = "X"
            elif chosenNumbers[j] in row4:
                row4[row4.index(chosenNumbers[j])] = "X"

            #Checking for win
            win(j, boardIndex)

    finalBoards.append([row0, row1, row2, row3, row4])

""" Checking if the board won """
def win(index: int, boardIndex: int):
    global winIndex
    global won
    global row0, row1, row2, row3, row4

    winArray = ["X","X","X","X","X"]

    col0 = [row0[0], row1[0], row2[0], row3[0], row4[0]]
    col1 = [row0[1], row1[1], row2[1], row3[1], row4[1]]
    col2 = [row0[2], row1[2], row2[2], row3[2], row4[2]]
    col3 = [row0[3], row1[3], row2[3], row3[3], row4[3]]
    col4 = [row0[4], row1[4], row2[4], row3[4], row4[4]]

    if row0 == winArray or row1 == winArray or row2 == winArray or row3 == winArray or row4 == winArray:
        try:
            _ = winIndex[boardIndex]
        except IndexError:
            winIndex.append(index)
            won = True

    elif col0 == winArray or col1 == winArray or col2 == winArray or col3 == winArray or col4 == winArray:
        try:
            _ = winIndex[boardIndex]
        except IndexError:
            winIndex.append(index)
            won = True

""" Find the sum of the unmarked numbers in the board """
def boardSum(index):
    global finalBoards

    sum = 0
    for row in finalBoards[index]:
        for i in row:
            if i != "X":
                sum += int(i)

    return sum

""" Main Function """
if __name__ == "__main__":
    
    file = open("input4.txt", "r")

    readings = file.readlines()

    # Making list of chosen Numbers
    chosenNumbers = readings[0].strip()
    chosenNumbers = chosenNumbers.split(",")

    readings.pop(0)

    # Settings up the boards in an array
    boards = []
    board = []

    for i in readings:

        if i == "\n":
            boards.append(board)
            board = []
        else:
            board.append(i.strip())

    boards.pop(0)
    boards.append(board)

    # Playing Bingo
    winIndex = []
    finalBoards = []

    for i in range(len(boards)):
        row0 = list(boards[i][0].split())
        row1 = list(boards[i][1].split())
        row2 = list(boards[i][2].split())
        row3 = list(boards[i][3].split())
        row4 = list(boards[i][4].split())

        # Marking chosen number And checking if won
        markChosen(i)

    # Part 1
    #
    # Choosing which board wins first
    winBoardIndex = winIndex.index(min(winIndex))

    winSum = boardSum(winBoardIndex)

    print("Part 1")
    print("Sum: {}\nNum: {}".format(winSum, chosenNumbers[min(winIndex)]))
    print("Score:", winSum * int(chosenNumbers[min(winIndex)]))

    print()

    # Part 2
    #
    # Choosing which board wins last
    loseBoardIndex = winIndex.index(max(winIndex))

    loseSum = boardSum(loseBoardIndex)
    
    print("Part 2")
    print("Sum: {}\nNum: {}".format(loseSum, chosenNumbers[max(winIndex)]))
    print("Score:", loseSum * int(chosenNumbers[max(winIndex)]))
