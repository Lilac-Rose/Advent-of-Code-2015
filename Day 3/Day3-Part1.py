with open("Day 3\part1-Input.txt") as f:
    data = f.read()

positionX = 0
positionY = 0

formattedData = ([*data])

houses = 0

coordinateList = ["0,0"]

for x in formattedData:
    if x == "<":
        positionX += -1
    if x == ">":
        positionX += 1
    if x == "v":
        positionY += -1
    if x == "^":
        positionY += 1
    coordinate = (str(positionX) + "," + str(positionY))
    coordinateList.append(coordinate)

coordinateList = list(set(coordinateList))

for y in coordinateList:
    houses += 1

print(houses)