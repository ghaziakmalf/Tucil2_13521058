import math

def distance(point1, point2):
    dis = 0
    for i in range(len(point1)):
        dis += (point1[i] - point2[i]) ** 2
    return math.sqrt(dis)

def sort(points):
    def quickSort(points, start, end):
        if start < end:
            pivot = partition(points, start, end)
            quickSort(points, start, pivot - 1)
            quickSort(points, pivot + 1, end)

    def partition(points, start, end):
        pivot = points[end][0]
        i = start - 1
        for j in range(start, end):
            if points[j][0] <= pivot:
                i += 1
                points[i], points[j] = points[j], points[i]
        points[i + 1], points[end] = points[end], points[i + 1]
        return i + 1

    quickSort(points, 0, len(points) - 1)
    return points