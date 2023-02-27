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
    process = commandInput()

    while (process == 1):
        nPoint, dimension = pointInput()

        points = []
        for i in range(nPoint):
            point = []
            for j in range(dimension):
                point.append(random.uniform(lowerLimit, upperLimit))
            points.append(point)

        start = time.time()

        points = sort(points)
        minDistance, point1, point2 = dividenconquer(points)

        end = time.time()

        plot(points, point1, point2, None)

        commandSave()
        save = commandInput()
        if (save == 1):
            saveConfig = input(str(WHITE + "\nInput Filename: " + RESET))

            if not os.path.exists("test/" + saveConfig):
                os.mkdir("test/" + saveConfig)

            with open("test/" + saveConfig + "/" + saveConfig + ".txt", "w") as f:
                f.write("Dua titik yang paling berdekatan:\n")
                f.write("Titik 1: " + ", ".join("{:.2f}".format(p) for p in point1))
                f.write("\n")
                f.write("Titik 2: " + ", ".join("{:.2f}".format(p) for p in point2))
                f.write("\nJaraknya adalah: {:.2f}".format(minDistance))
                f.write("\nWaktu eksekusi: {:.2f} ms".format((end - start) * 1000))
                f.write("\n")
                f.write(platform.processor())

            plot(points, point1, point2, "test/" + saveConfig + "/" + saveConfig + ".png")
            
            print(LIGHT_GREEN + "\nFile saved!" + RESET)

        print(LIGHT_GREEN + "\nDo you want to try again?\n" + RESET)
        commandStart()
        process = commandInput()
    
    print(LIGHT_GREEN + "\nThank you for using Shortest Distance Solver!\n" + RESET)

if __name__ == "__main__":
    upperLimit = 1000.0
    lowerLimit = -1000.0
    main()