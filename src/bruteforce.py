from utility import distance

def bruteforce(points):
    minDistance = distance(points[0], points[1])
    point1 = points[0]
    point2 = points[1]
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dis = distance(points[i], points[j])
            if dis < minDistance:
                minDistance = dis
                point1 = points[i]
                point2 = points[j]
    return minDistance, point1, point2