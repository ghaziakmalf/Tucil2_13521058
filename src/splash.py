import time
from colors import *

def splash():
    print(LIGHT_GREEN)
    print("    /$$      /$$/$$$$$$$$/$$       /$$$$$$  /$$$$$$ /$$      /$$/$$$$$$$$/$$")
    print("   | $$  /$ | $| $$_____| $$      /$$__  $$/$$__  $| $$$    /$$| $$_____| $$")
    print("   | $$ /$$$| $| $$     | $$     | $$  \\__| $$  \\ $| $$$$  /$$$| $$     | $$")
    print("   | $$/$$ $$ $| $$$$$  | $$     | $$     | $$  | $| $$ $$/$$ $| $$$$$  | $$")
    print("   | $$$$_  $$$| $$__/  | $$     | $$     | $$  | $| $$  $$$| $| $$__/  |__/")
    print("   | $$$/ \\  $$| $$     | $$     | $$    $| $$  | $| $$\\  $ | $| $$         ")
    print("   | $$/   \\  $| $$$$$$$| $$$$$$$|  $$$$$$|  $$$$$$| $$ \\/  | $| $$$$$$$$/$$")
    print("   |__/     \\__|________|________/\\______/ \\______/|__/     |__|________|__/")

    print(WHITE)
    print("Welcome to Shortest Distance Solver")

    print(YELLOW)
    print("A " + CROSSED + "Group" + RESET + YELLOW + " Solo Project")
    print("Made By " + UNDERLINE + "Ghazi Akmal Fauzan (13521058)" + RESET)

    print(LIGHT_RED)
    print("Loading", end="", flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)

    print(WHITE)
    print("Solver Loaded!")
    print(RESET)