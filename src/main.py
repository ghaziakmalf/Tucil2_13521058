import os
import time
import random
import platform

from colors import *
from splash import *
from command import *
from plot import *
from utility import *
from dividenconquer import *
from bruteforce import *

def main():
    splash()
    commandStart()
    process = commandInput1()

    while (process == 1):
        nPoint, dimension = pointInput()

        print("")
        commandInputOption()
        option = commandInput1()
        points = []

        if (option == 1):
            for i in range(nPoint):
                point = []
                for j in range(dimension):
                    point.append(random.uniform(lowerLimit, upperLimit))
                points.append(point)
        else:
            print("")
            for i in range(nPoint):
                point = []
                for j in range(dimension):
                    point.append(float(input(str(WHITE + "Input Point " + str(i+1) + " Dimension " + str(j+1) + ": " + RESET))))
                points.append(point)

        print("")
        commandAlgorithm()
        algorithm = commandInput2()

        if (algorithm == 1) or (algorithm == 3):
            startBF = time.time()

            points = sort(points)
            minDistanceBF, point1BF, point2BF, nCalculationBF = bruteforce(points)

            endBF = time.time()

            print(WHITE + "\n==============" + LIGHT_RED + " BRUTE FORCE " + WHITE + "===============")
            print(WHITE + "Two points with shortest distance: ")
            print(WHITE + "Point 1: " + YELLOW + ", ".join("{:.2f}".format(p) for p in point1BF))
            print(WHITE + "Point 2: " + YELLOW + ", ".join("{:.2f}".format(p) for p in point2BF))
            print(WHITE + "Distance: " + YELLOW + "{:.2f}".format(minDistanceBF))
            print(WHITE + "Number of calculation: " + YELLOW + "{}".format(nCalculationBF))
            print(WHITE + "Execution time: " + YELLOW + "{:.2f} ms".format((endBF - startBF) * 1000))
            print(WHITE + "Processor: " + YELLOW + "{}".format(platform.processor()) + RESET)
            plot("BRUTE FORCE", points, point1BF, point2BF, None)
        
        if (algorithm == 2) or (algorithm == 3):
            startDnC = time.time()

            points = sort(points)
            minDistanceDnC, point1DnC, point2DnC, nCalculationDnC = dividenconquer(points)

            endDnC = time.time()

            print(WHITE + "\n===========" + LIGHT_RED + " DIVIDE AND CONQUER " + WHITE + "===========")
            print(WHITE + "Two points with shortest distance:")
            print(WHITE + "Point 1: " + YELLOW + ", ".join("{:.2f}".format(p) for p in point1DnC))
            print(WHITE + "Point 2: " + YELLOW + ", ".join("{:.2f}".format(p) for p in point2DnC))
            print(WHITE + "Distance: " + YELLOW + "{:.2f}".format(minDistanceDnC))
            print(WHITE + "Number of calculation: " + YELLOW + "{}".format(nCalculationDnC))
            print(WHITE + "Execution time: " + YELLOW + "{:.2f} ms".format((endDnC - startDnC) * 1000))
            print(WHITE + "Processor: " + YELLOW + "{}".format(platform.processor()) + RESET)
            plot("DIVIDE AND CONQUER", points, point1BF, point2BF, None)

        print("")
        commandSave()
        save = commandInput1()
        if (save == 1):
            saveConfig = input(str(WHITE + "\nInput Filename: " + RESET))

            if not os.path.exists("test"):
                os.mkdir("test")
            if not os.path.exists("test/" + saveConfig):
                os.mkdir("test/" + saveConfig)

            if (algorithm == 1):
                with open("test/" + saveConfig + "/" + saveConfig + ".txt", "w") as f:
                    f.write("==============" + " BRUTE FORCE " + "===============\n")
                    f.write("Two points with shortest distance: \n")
                    f.write("Point 1: " + ", ".join("{:.2f}".format(p) for p in point1BF) + "\n")
                    f.write("Point 2: " + ", ".join("{:.2f}".format(p) for p in point2BF) + "\n")
                    f.write("Distance: " + "{:.2f}".format(minDistanceBF) + "\n")
                    f.write("Number of calculation: " + "{}".format(nCalculationBF) + "\n")
                    f.write("Execution time: " + "{:.2f} ms".format((endBF - startBF) * 1000) + "\n")
                    f.write("Processor: " + "{}".format(platform.processor()) + "\n")
                plot("BRUTE FORCE", points, point1BF, point2BF, "test/" + saveConfig + "/" + saveConfig + ".png")

            elif (algorithm == 2):
                with open("test/" + saveConfig + "/" + saveConfig + ".txt", "a") as f:
                    f.write("\n===========" + " DIVIDE AND CONQUER " + "===========\n")
                    f.write("Two points with shortest distance:\n")
                    f.write("Point 1: " + ", ".join("{:.2f}".format(p) for p in point1DnC) + "\n")
                    f.write("Point 2: " + ", ".join("{:.2f}".format(p) for p in point2DnC) + "\n")
                    f.write("Distance: " + "{:.2f}".format(minDistanceDnC) + "\n")
                    f.write("Number of calculation: " + "{}".format(nCalculationDnC) + "\n")
                    f.write("Execution time: " + "{:.2f} ms".format((endDnC - startDnC) * 1000) + "\n")
                    f.write("Processor: " + "{}".format(platform.processor()) + "\n")
                plot("DIVIDE AND CONQUER", points, point1BF, point2BF, "test/" + saveConfig + "/" + saveConfig + ".png")
            
            else:
                with open("test/" + saveConfig + "/" + saveConfig + ".txt", "w") as f:
                    f.write("==============" + " BRUTE FORCE " + "===============\n")
                    f.write("Two points with shortest distance: \n")
                    f.write("Point 1: " + ", ".join("{:.2f}".format(p) for p in point1BF) + "\n")
                    f.write("Point 2: " + ", ".join("{:.2f}".format(p) for p in point2BF) + "\n")
                    f.write("Distance: " + "{:.2f}".format(minDistanceBF) + "\n")
                    f.write("Number of calculation: " + "{}".format(nCalculationBF) + "\n")
                    f.write("Execution time: " + "{:.2f} ms".format((endBF - startBF) * 1000) + "\n")
                    f.write("Processor: " + "{}".format(platform.processor()) + "\n")
                    f.write("")
                    f.write("\n===========" + " DIVIDE AND CONQUER " + "===========\n")
                    f.write("Two points with shortest distance:\n")
                    f.write("Point 1: " + ", ".join("{:.2f}".format(p) for p in point1DnC) + "\n")
                    f.write("Point 2: " + ", ".join("{:.2f}".format(p) for p in point2DnC) + "\n")
                    f.write("Distance: " + "{:.2f}".format(minDistanceDnC) + "\n")
                    f.write("Number of calculation: " + "{}".format(nCalculationDnC) + "\n")
                    f.write("Execution time: " + "{:.2f} ms".format((endDnC - startDnC) * 1000) + "\n")
                    f.write("Processor: " + "{}".format(platform.processor()) + "\n")
                plot("BRUTE FORCE", points, point1BF, point2BF, "test/" + saveConfig + "/" + saveConfig + "BF.png")
                plot("DIVIDE AND CONQUER", points, point1BF, point2BF, "test/" + saveConfig + "/" + saveConfig + "DnC.png")
            
            print(LIGHT_GREEN + "\nFile saved!" + RESET)

        print(LIGHT_GREEN + "\nDo you want to try again?\n" + RESET)
        commandStart()
        process = commandInput1()
    
    print(LIGHT_GREEN + "\nThank you for using Shortest Distance Solver!\n" + RESET)

if __name__ == "__main__":
    upperLimit = 1000.0
    lowerLimit = -1000.0
    main()