# Advent Of coding 
# Day 16
#
# By Shivoy Arora

""" Decode the binary message """
def Decode(binary):
    global versionSum

    # endIndex = None
    # subPackets = 0

    index = 0
    while binary[index:] != "" and int(binary[index:]) != 0:

        # if endIndex and index == endIndex:
        #     binary = "0"*(3-(len(binary[index+1:])%4)) + binary[index+1:]
        #     index = 0
        #     endIndex = None

        version = BinToDecimal(binary[index:index+3])
        # print("Version:", version)
        versionSum += version
        index += 3
        type = BinToDecimal(binary[index:index+3])
        index += 3

        # literal type packet
        if type == 4:
            literalBin = ""

            run = True
            while run:
                if binary[index] == "0":
                    literalBin += binary[index+1:index+5]
                    index += 5
                    run = False
                else:
                    literalBin += binary[index+1:index+5]
                    index += 5
            # print("Literal Num:",BinToDecimal(literalBin))

            # if numSubPackets:
            #     subPackets += 1
            #     if numSubPackets == subPackets:
            #         subPackets = 0
            #         binary = "0"*(3-(len(binary[index+1:])%4)) + binary[index+1:]
            #         index = 0
            

        # operator type packet
        else:
            if binary[index] == "0":
                num = BinToDecimal(binary[index+1:index+16])
                index += 16
                # print("type1 ops\n")
                Decode(binary[index:index+num])
                index += num

            elif binary[index] == "1":
                # numSubPackets = BinToDecimal(binary[index+1:index+12])
                index += 12
                # print("type2 ops\n")

""" Convert hexadecimal input to binary """
def HexToBin():
    global readings

    # Dictionary with hex keys and their binary values
    hexToBin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    binary = ""

    for i in readings:
        binary += hexToBin[i]

    return binary

""" Convert binary to decimal """
def BinToDecimal(binary):
    decimal = 0

    for i in range(len(binary)):
        decimal += int(binary[len(binary) - i - 1]) * (2**i)

    return decimal

""" Main Function """
file = open("input/input16.txt", "r")
# file = open("input/test.txt", "r")

readings = file.readline().strip()

binary = HexToBin()
# print("binary:", binary,"\n")

versionSum = 0

index = 0
Decode(binary)

print("Part 1")
print("Version Sum:", versionSum)

print()

