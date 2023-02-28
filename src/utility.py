import math

# Calculate the distance between two points
def distance(point1, point2):
    dis = 0
    for i in range(len(point1)):
        dis += (point1[i] - point2[i]) ** 2
    return math.sqrt(dis)

# Sort the points
def sort(points):
    if len(points) <= 1:
        return points
    else:
        pivot = points[0]
        less = []
        greater = []
        for i in range(1, len(points)):
            if points[i] < pivot:
                less.append(points[i])
            else:
                greater.append(points[i])
        return sort(less) + [pivot] + sort(greater)