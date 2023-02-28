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
        print("")
        commandInputOption()
        option = commandInput2()
        points = []

        if (option == 1):
            nPoint, dimension = pointInput()
            for i in range(nPoint):
                point = []
                for j in range(dimension):
                    point.append(random.uniform(lowerLimit, upperLimit))
                points.append(point)
        elif (option == 2):
            nPoint, dimension = pointInput()
            print("")
            for i in range(nPoint):
                point = []
                for j in range(dimension):
                    while True:
                        inputNumber = input(WHITE + "Input Point " + str(i+1) + " Dimension " + str(j+1) + ": " + RESET)
                        try:
                            inputNumber = float(inputNumber)
                            point.append(inputNumber)
                            break
                        except ValueError:
                            print(LIGHT_RED + "\nInput is not a number! Please re-enter.\n" + RESET)
                points.append(point)
        else:
            print("")
            while (True):
                print(LIGHT_GREEN + "Input format (example.txt). Put inside 'test' folder." + RESET)
                fileName = input(WHITE + "Input Filename: " + RESET)
                if os.path.isfile("test/" + fileName):
                    file = open("test/" + fileName, "r")
                    for line in file:
                        point = []
                        for i in line.split():
                            point.append(float(i))
                        points.append(point)
                    file.close()
                    break
                else:
                    print(LIGHT_RED + "\nFile not found! Please re-enter.\n" + RESET)

        print("")
        commandAlgorithm()
        algorithm = commandInput2()

        if (algorithm == 1) or (algorithm == 3):
            startBF = time.time()

            pointsBF = sort(points)
            minDistanceBF, point1BF, point2BF, nCalculationBF = bruteforce(pointsBF)

            endBF = time.time()

            print(WHITE + "\n==============" + LIGHT_RED + " BRUTE FORCE " + WHITE + "===============")
            print(WHITE + "Two points with shortest distance: ")
            print(WHITE + "Point 1: " + YELLOW + ", ".join("{:.2f}".format(p) for p in point1BF))
            print(WHITE + "Point 2: " + YELLOW + ", ".join("{:.2f}".format(p) for p in point2BF))
            print(WHITE + "Distance: " + YELLOW + "{:.2f}".format(minDistanceBF))
            print(WHITE + "Number of calculation: " + YELLOW + "{}".format(nCalculationBF))
            print(WHITE + "Execution time: " + YELLOW + "{:.2f} ms".format((endBF - startBF) * 1000))
            print(WHITE + "Processor: " + YELLOW + "{}".format(platform.processor()) + RESET)
            plot("BRUTE FORCE", pointsBF, point1BF, point2BF, None)
        
        if (algorithm == 2) or (algorithm == 3):
            startDnC = time.time()

            pointsDnC = sort(points)
            minDistanceDnC, point1DnC, point2DnC, nCalculationDnC = dividenconquer(pointsDnC)

            endDnC = time.time()

            print(WHITE + "\n===========" + LIGHT_RED + " DIVIDE AND CONQUER " + WHITE + "===========")
            print(WHITE + "Two points with shortest distance:")
            print(WHITE + "Point 1: " + YELLOW + ", ".join("{:.2f}".format(p) for p in point1DnC))
            print(WHITE + "Point 2: " + YELLOW + ", ".join("{:.2f}".format(p) for p in point2DnC))
            print(WHITE + "Distance: " + YELLOW + "{:.2f}".format(minDistanceDnC))
            print(WHITE + "Number of calculation: " + YELLOW + "{}".format(nCalculationDnC))
            print(WHITE + "Execution time: " + YELLOW + "{:.2f} ms".format((endDnC - startDnC) * 1000))
            print(WHITE + "Processor: " + YELLOW + "{}".format(platform.processor()) + RESET)
            plot("DIVIDE AND CONQUER", pointsDnC, point1DnC, point2DnC, None)

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
                    f.write("Points:\n")
                    for i in range(len(pointsBF)):
                        f.write("(" + ", ".join("{:.2f}".format(p) for p in pointsBF[i]) + ")\n")
                    f.write("\n==============" + " BRUTE FORCE " + "===============\n")
                    f.write("Two points with shortest distance: \n")
                    f.write("Point 1: " + ", ".join("{:.2f}".format(p) for p in point1BF) + "\n")
                    f.write("Point 2: " + ", ".join("{:.2f}".format(p) for p in point2BF) + "\n")
                    f.write("Distance: " + "{:.2f}".format(minDistanceBF) + "\n")
                    f.write("Number of calculation: " + "{}".format(nCalculationBF) + "\n")
                    f.write("Execution time: " + "{:.2f} ms".format((endBF - startBF) * 1000) + "\n")
                    f.write("Processor: " + "{}".format(platform.processor()) + "\n")
                plot("BRUTE FORCE", pointsBF, point1BF, point2BF, "test/" + saveConfig + "/" + saveConfig + ".png")

            elif (algorithm == 2):
                with open("test/" + saveConfig + "/" + saveConfig + ".txt", "a") as f:
                    f.write("Points:\n")
                    for i in range(len(pointsDnC)):
                        f.write("(" + ", ".join("{:.2f}".format(p) for p in pointsDnC[i]) + ")\n")
                    f.write("\n===========" + " DIVIDE AND CONQUER " + "===========\n")
                    f.write("Two points with shortest distance:\n")
                    f.write("Point 1: " + ", ".join("{:.2f}".format(p) for p in point1DnC) + "\n")
                    f.write("Point 2: " + ", ".join("{:.2f}".format(p) for p in point2DnC) + "\n")
                    f.write("Distance: " + "{:.2f}".format(minDistanceDnC) + "\n")
                    f.write("Number of calculation: " + "{}".format(nCalculationDnC) + "\n")
                    f.write("Execution time: " + "{:.2f} ms".format((endDnC - startDnC) * 1000) + "\n")
                    f.write("Processor: " + "{}".format(platform.processor()) + "\n")
                plot("DIVIDE AND CONQUER", pointsDnC, point1DnC, point2DnC, "test/" + saveConfig + "/" + saveConfig + ".png")
            
            else:
                with open("test/" + saveConfig + "/" + saveConfig + ".txt", "w") as f:
                    f.write("Points:\n")
                    for i in range(len(points)):
                        f.write("(" + ", ".join("{:.2f}".format(p) for p in points[i]) + ")\n")
                        
                    f.write("\n==============" + " BRUTE FORCE " + "===============\n")
                    f.write("Two points with shortest distance: \n")
                    f.write("Point 1: " + ", ".join("{:.2f}".format(p) for p in point1BF) + "\n")
                    f.write("Point 2: " + ", ".join("{:.2f}".format(p) for p in point2BF) + "\n")
                    f.write("Distance: " + "{:.2f}".format(minDistanceBF) + "\n")
                    f.write("Number of calculation: " + "{}".format(nCalculationBF) + "\n")
                    f.write("Execution time: " + "{:.2f} ms".format((endBF - startBF) * 1000) + "\n")
                    f.write("Processor: " + "{}".format(platform.processor()) + "\n")

                    f.write("\n===========" + " DIVIDE AND CONQUER " + "===========\n")
                    f.write("Two points with shortest distance:\n")
                    f.write("Point 1: " + ", ".join("{:.2f}".format(p) for p in point1DnC) + "\n")
                    f.write("Point 2: " + ", ".join("{:.2f}".format(p) for p in point2DnC) + "\n")
                    f.write("Distance: " + "{:.2f}".format(minDistanceDnC) + "\n")
                    f.write("Number of calculation: " + "{}".format(nCalculationDnC) + "\n")
                    f.write("Execution time: " + "{:.2f} ms".format((endDnC - startDnC) * 1000) + "\n")
                    f.write("Processor: " + "{}".format(platform.processor()) + "\n")
                plot("BRUTE FORCE", pointsBF, point1BF, point2BF, "test/" + saveConfig + "/" + saveConfig + "BF.png")
                plot("DIVIDE AND CONQUER", pointsDnC, point1DnC, point2DnC, "test/" + saveConfig + "/" + saveConfig + "DnC.png")
            
            print(LIGHT_GREEN + "\nAdditional Information Added into txt File" + RESET)
            print(LIGHT_GREEN + "File saved!" + RESET)

        print(LIGHT_GREEN + "\nDo you want to try again?\n" + RESET)
        commandStart()
        process = commandInput1()
    
    print(LIGHT_GREEN + "\nThank you for using Shortest Distance Solver!\n" + RESET)

if __name__ == "__main__":
    upperLimit = 1000.0
    lowerLimit = -1000.0
    main()