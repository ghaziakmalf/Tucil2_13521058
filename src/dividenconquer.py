from utility import distance

def dividenconquer(points):
    if len(points) == 2:
        return distance(points[0], points[1]), points[0], points[1]
    
    elif len(points) == 3:
        minDistance = distance(points[0], points[1])
        point1 = points[0]
        point2 = points[1]
        # Brute Force
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = distance(points[i], points[j])
                if dis < minDistance:
                    minDistance = dis
                    point1 = points[i]
                    point2 = points[j]
        return minDistance, point1, point2
    
    else:
        mid = len(points) // 2
        leftMinDistance, leftPoint1, leftPoint2 = dividenconquer(points[:mid])
        rightMinDistance, rightPoint1, rightPoint2 = dividenconquer(points[mid:])
        if leftMinDistance < rightMinDistance:
            minDistance = leftMinDistance
            point1 = leftPoint1
            point2 = leftPoint2
        else:
            minDistance = rightMinDistance
            point1 = rightPoint1
            point2 = rightPoint2

        midX = points[mid][0]
        minPoints = []
        for point in points:
            if abs(point[0] - midX) < minDistance:
                minPoints.append(point)

        # Brute Force
        for i in range(len(minPoints)):
            for j in range(i+1, len(minPoints)):
                dis = distance(minPoints[i], minPoints[j])
                if dis < minDistance:
                    minDistance = dis
                    point1 = minPoints[i]
                    point2 = minPoints[j]
        
        return minDistance, point1, point2