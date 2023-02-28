# Finding the Closest Point Pair with _Divide and Conquer_ Algorithm

## Program Description
In short, the _Divide and Conquer_ algorithm has the principle of breaking the existing problem into several small parts so that it is easier to solve. The general steps of the Divide and Conquer algorithm are:

1. __Divide__: Divide the problem into several sub-problems that are similar to the original problem but smaller in size (ideally almost the same size);
2. __Conquer__: Solve (resolve) each sub-problem (recursively);
3. __Combine__: Combining the solutions of each problem so as to form the original problem solution.

In this project, the author was tasked to develop an algorithm to find a pair of closest points in the 3D plane. Suppose there are n points in 3D space. Each point P in space is represented by coordinates P = (x, y, z). Find a pair of points that are the shortest distance from each other.

## Algorithm Used
- Brute Force (for comparison)
- Divide and Conquer

## Program Requirement
- Python (tested version 3.11.0)
- Install all libraries used below

## Libraries Used
- math
- time
- random
- platform
- matplotlib
- PILLOW
- os

## Program Structure
```
.
├── doc/
│   ├── Tucil2_K2_13521058_Ghazi Akmal Fauzan.pdf
│   └── Tucil2-Stima-2023.pdf
├── src/
│   ├── bruteforce.py
│   ├── colors.py
│   ├── command.py
│   ├── dividenconquer.py
│   ├── main.py
│   ├── plot.py
|   ├── splash.py
│   └── utility.py
├── test/
├── .gitignore
├── README.md
├── RunnerPy.bat
└── RunnerPython.bat
```

## How To Run
To run the program in the terminal _root directory_, run the command __RunnerPy.bat__ or __RunnerPython.bat__ (on windows). The runner used depends on the latest version of python on the PC (you can check using 'py --version' and 'python --version'), because on some PCs there is a difference between using py and python.
```
./RunnerPy.bat

or

./RunnerPython.bat

or

double click the runner you want to use
```
The program can also be run by directly compiling _main.py_ with the following command.
```
py src/main.py

or

python src/main.py
```
However, it is better to run the program using _Runner_ because it will automatically delete __pycache__ when exiting the program.

## Author
13521058 - Ghazi Akmal Fauzan