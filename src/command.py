from colors import *

# Start/Exit
def commandStart():
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|               START/EXIT               |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " START")
    print(LIGHT_RED + "2." + WHITE + " EXIT")

# Pick algorithm
def commandAlgorithm():
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|             PICK ALGORITHM             |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " BRUTE FORCE")
    print(LIGHT_RED + "2." + WHITE + " DIVIDE AND CONQUER")
    print(LIGHT_RED + "3." + WHITE + " BOTH")

# Input options
def commandInputOption():
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|             INPUT OPTIONS              |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " RANDOM")
    print(LIGHT_RED + "2." + WHITE + " MANUAL")
    print(LIGHT_RED + "3." + WHITE + " FILE")

# Save solution
def commandSave():
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|             SAVE SOLUTION?             |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " YES")
    print(LIGHT_RED + "2." + WHITE + " NO")

# 1/2 Input command
def commandInput1():
    while (True):
        Input = input(WHITE + ">> " + RESET)
        try:
            Input = int(Input)
            if (Input == 1 or Input == 2):
                break
            else:
                print(LIGHT_RED + "\nPlease enter a valid input! (1/2)" + RESET)
        except ValueError:
            print(LIGHT_RED + "\nInput is not an integer! Please re-enter." + RESET)

    return Input

# 1/2/3 Input command
def commandInput2():
    while (True):
        Input = input(WHITE + ">> " + RESET)
        try:
            Input = int(Input)
            if (Input == 1 or Input == 2 or Input == 3):
                break
            else:
                print(LIGHT_RED + "\nPlease enter a valid input! (1/2/3)" + RESET)
        except ValueError:
            print(LIGHT_RED + "\nInput is not an integer! Please re-enter." + RESET)

    return Input

# nPoint and dimension input
def pointInput():
    while (True):
        nPoint = input(WHITE + "\nEnter the number of points: " + RESET)
        try:
            nPoint = int(nPoint)
            if nPoint < 2:
                print(LIGHT_RED + "\nThe minimum number of points is 2! Please re-enter." + RESET)
            else:
                break
        except ValueError:
            print(LIGHT_RED + "\nInput is not an integer! Please re-enter." + RESET)

    while (True):
        dimension = input(WHITE + "Enter the number of dimensions: " + RESET)
        try:
            dimension = int(dimension)
            if dimension < 1:
                print(LIGHT_RED + "\nThe minimum number of dimensions is 1! Please re-enter.\n" + RESET)
            else:
                break
        except ValueError:
            print(LIGHT_RED + "\nInput is not a number! Please re-enter.\n" + RESET)

    return nPoint, dimension