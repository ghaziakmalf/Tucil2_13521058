from utility import distance

def dividenconquer(points, nCalculation = 0):
    if len(points) == 2:
        nCalculation += 1
        return distance(points[0], points[1]), points[0], points[1], nCalculation
    
    elif len(points) == 3:
        minDistance = distance(points[0], points[1])
        point1 = points[0]
        point2 = points[1]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = distance(points[i], points[j])
                nCalculation += 1
                if dis < minDistance:
                    minDistance = dis
                    point1 = points[i]
                    point2 = points[j]
        return minDistance, point1, point2, nCalculation
    
    else:
        mid = len(points) // 2
        leftMinDistance, leftPoint1, leftPoint2, nCalculation = dividenconquer(points[:mid], nCalculation)
        rightMinDistance, rightPoint1, rightPoint2, nCalculation = dividenconquer(points[mid:], nCalculation)
        if leftMinDistance < rightMinDistance:
            minDistance = leftMinDistance
            point1 = leftPoint1
            point2 = leftPoint2
        else:
            minDistance = rightMinDistance
            point1 = rightPoint1
            point2 = rightPoint2

        midPoint = points[mid][0]
        midPoints = []
        for i in range(len(points)):
            if (midPoint - minDistance) < points[i][0] < (midPoint + minDistance):
                midPoints.append(points[i])

        for i in range(len(midPoints)):
            for j in range(i+1, len(midPoints)):
                calculate = True
                for k in range(len(midPoints[i])):
                    if abs(midPoints[i][k] - midPoints[j][k]) > minDistance:
                        calculate = False
                        break
                if calculate:
                    dis = distance(midPoints[i], midPoints[j])
                    nCalculation += 1
                    if dis < minDistance:
                        minDistance = dis
                        point1 = midPoints[i]
                        point2 = midPoints[j]

        return minDistance, point1, point2, nCalculation