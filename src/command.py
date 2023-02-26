from colors import *

def commandStart():
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|               START/EXIT               |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " START")
    print(LIGHT_RED + "2." + WHITE + " EXIT")

def commandSave():
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|             SAVE SOLUTION?             |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " YES")
    print(LIGHT_RED + "2." + WHITE + " NO" + RESET)

def commandInput():
    while (True):
        Input = int(input(WHITE + ">> " + RESET))
        if (Input == 1 or Input == 2):
            break
        else:
            print(LIGHT_RED + "\nPlease enter a valid input! (1/2)" + RESET)

    return Input

def pointInput():
    while (True):
        nPoint = int(input(WHITE + "\nEnter the number of points: " + RESET))
        if nPoint < 2:
            print(LIGHT_RED + "\nThe minimum number of points is 2! Please re-enter." + RESET)
        else:
            break

    while (True):
        dimension = int(input(WHITE + "Enter the number of dimensions: " + RESET))
        if dimension < 1:
            print(LIGHT_RED + "\nThe minimum number of dimensions is 1! Please re-enter.\n" + RESET)
        else:
            break

    return nPoint, dimension