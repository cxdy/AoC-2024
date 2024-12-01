def calculateTotalDistance(leftList, rightList):

    leftList.sort()
    rightList.sort()

    totalDistance = sum(abs(l - r) for l, r in zip(leftList, rightList))

    return totalDistance

def readInputs(filename):

    leftList = []
    rightList = []

    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            leftList.append(left)
            rightList.append(right)

    return leftList, rightList

leftList, rightList = readInputs('input.txt')

print(f"Total distance: {calculateTotalDistance(leftList, rightList)}")