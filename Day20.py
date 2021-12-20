# Advent Of coding 
# Day 20
#
# By Shivoy Arora

""" Increasing the size of the img to account for infinite size """
def incImg(step: bool):
    global img

    if not step % 2:
        pixel = "."
    else:
        pixel = "#"

    for i in range(len(img)):
        img[i] = pixel+img[i]+pixel
    img.append(pixel*len(img[i]))
    img.insert(0, pixel*len(img[i]))

""" Make bin num """
def EnhancePixel(i,j, step):
    global imgEnchance, img
 
    binary = ""
    try:
        if i > 0 and j > 0:
            binary += "1" if img[i-1][j-1] == "#" else "0"
        else:
            binary += "0" if not step%2 else "1"
    except IndexError:
        binary += "0" if not step%2 else "1"
    try:
        if i > 0:
            binary += "1" if img[i-1][j] == "#" else "0"
        else:
            binary += "0" if not step%2 else "1"
    except IndexError:
        binary += "0" if not step%2 else "1"
    try:
        if i > 0:
            binary += "1" if img[i-1][j+1] == "#" else "0"
        else:
            binary += "0" if not step%2 else "1"
    except IndexError:
        binary += "0" if not step%2 else "1"
    try:
        if j > 0:
            binary += "1" if img[i][j-1] == "#" else "0"
        else:
            binary += "0" if not step%2 else "1"
    except IndexError:
        binary += "0" if not step%2 else "1"
    try:
        binary += "1" if img[i][j] == "#" else "0"
    except IndexError:
        binary += "0" if not step%2 else "1"
    try:
        binary += "1" if img[i][j+1] == "#" else "0"
    except IndexError:
        binary += "0" if not step%2 else "1"
    try:
        if j > 0:
            binary += "1" if img[i+1][j-1] == "#" else "0"
        else:
            binary += "0" if not step%2 else "1"
    except IndexError:
        binary += "0" if not step%2 else "1"
    try:
        binary += "1" if img[i+1][j] == "#" else "0"
    except IndexError:
        binary += "0" if not step%2 else "1"
    try:
        binary += "1" if img[i+1][j+1] == "#" else "0"
    except IndexError:
        binary += "0" if not step%2 else "1"

    index = int(binary, base=2)

    return imgEnchance[index]

def EnhanceImg(step):
    global img

    enhanced = [["." for _ in range(len(img[0]))] for _ in range(len(img))]

    for i in range(len(img)):
        for j in range(len(img[i])):
            enhanced[i][j] = EnhancePixel(i,j, step)

    return enhanced.copy()
    
""" Main Function """
file = open("input/input20.txt", "r")

imgEnchance = file.readline().strip()
file.readline()

img = [i.strip() for i in file.readlines()]

# Part 1

# increasing size of img
for step in range(2):
    incImg(step)
    enhanced = EnhanceImg(step)
    img = ["".join(enhanced[i]) for i in range(len(enhanced))]

ctr = 0
for i in img:
    for j in i:
        if j == "#":
            ctr += 1

print("No. of lit pixels:", ctr)

print()

# Part 2
for step in range(2, 50):
    incImg(step)
    enhanced = EnhanceImg(step)
    img = ["".join(enhanced[i]) for i in range(len(enhanced))]

ctr = 0
for i in img:
    for j in i:
        if j == "#":
            ctr += 1
            
print("No. of lit pixels:", ctr)
