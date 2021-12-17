# Advent Of coding 
# Day 17
#
# By Shivoy Arora

def WillHit(xVelocity, yVelocity):
    global trenchX, trenchY

    x = 0
    y = 0

    while True:
        x += xVelocity
        y += yVelocity

        if x in trenchX and y in trenchY:
            return True
        if xVelocity > 0:
            xVelocity -= 1
        yVelocity -= 1

        if x > max(trenchX) or y < min(trenchY):
            return False

# My puzzle input
trenchX = range(192, 252)
trenchY = range(-89,-58)

hits = []

xVelocity = 0
while xVelocity <= max(trenchX):
    yVelocity = abs(min(trenchY))
    
    while yVelocity >= min(trenchY):

        if WillHit(xVelocity, yVelocity):
            hits.append((xVelocity, yVelocity))

        yVelocity -= 1
    
    xVelocity += 1

# Part 1
maxYVel = None
for i in hits:
    if not maxYVel or maxYVel < i[1]:
        maxYVel = i[1]

maxY = maxYVel*(maxYVel+1)/2

print("Part 1")
print("Max Height:", maxY)

print()

# Part 2
print("Part 2")
print("Total distant Velocities: ", len(hits))
