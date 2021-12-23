# Advent Of coding 
# Day 21
#
# By Shivoy Arora

def FindModulus(num, divisor):
    return num%divisor if num%divisor != 0 else divisor

""" Main Function """
player1pos = 3
player2pos = 10

diceRolls = 1

score1 = 0
score2 = 0
winScore = 0

# Part 1
while True:

    if diceRolls%2:
        player1pos = FindModulus((player1pos + (FindModulus(diceRolls, 100)) + FindModulus(diceRolls+1, 100) + FindModulus(diceRolls+2, 100)), 10)
        score1 += player1pos
    else:
        player2pos = FindModulus((player2pos + (FindModulus(diceRolls, 100)) + FindModulus(diceRolls+1, 100) + FindModulus(diceRolls+2, 100)), 10)
        score2 += player2pos

    diceRolls += 3

    if score1 >= 1000:
        winScore = score2*(diceRolls-1)
        break
    elif score2 >= 1000:
        winScore = score1*(diceRolls-1)
        break

print("Wining points:", winScore)

print()

# Part 2
win1 = 0
win2 = 0

diceRollSum = []
for one in (1, 2, 3):
    for two in (1, 2, 3):
        for three in (1, 2, 3):
            diceRollSum.append(one+two+three)

# struct :- pos1, score1, pos2, score2, turn
gameInitial = (3,0,10,0,1)
games = {gameInitial: 1}
while games:
    newGames = dict()

    for game, universes in games.items():
        playerTurn = game[4]
        if playerTurn == 1:
            pos, score = game[0], game[1]
        else:
            pos, score = game[2], game[3]
        
        for roll in diceRollSum:
            newPos = FindModulus(pos + roll, 10)

            newScore = score + newPos

            if newScore >= 21:
                if playerTurn == 1:
                    win1 += universes
                else:
                    win2 += universes

            else:
                if playerTurn == 1:
                    val = (newPos, newScore, game[2], game[3], 2)
                else:
                    val = (game[0], game[1], newPos, newScore, 1)

                try:
                    _ = newGames[val]
                    newGames[val] += universes
                except KeyError:
                    newGames[val] = universes
    
    games = newGames

print("Part 2")
print("Max no of wins:", max(win1, win2))
