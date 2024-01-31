with open("Day 3\part2-Input.txt") as f:
    data = f.read()

santaPositionX = 0
santaPositionY = 0

roboSantaPositionX = 0
roboSantaPositionY = 0

formattedData = ([*data])

houses = 0

santaCoordinateList = ["0,0"]
roboSantaCoordinateList = ["0,0"]

santaFormattedData = formattedData[::2]
roboSantaFormattedData = formattedData
del roboSantaFormattedData[0]
roboSantaFormattedData = roboSantaFormattedData[::2]


for x in santaFormattedData:
    if x == "<":
        santaPositionX += -1
    if x == ">":
        santaPositionX += 1
    if x == "v":
        santaPositionY += -1
    if x == "^":
        santaPositionY += 1
    coordinate = (str(santaPositionX) + "," + str(santaPositionY))
    santaCoordinateList.append(coordinate)

for x in roboSantaFormattedData:
    if x == "<":
        roboSantaPositionX += -1
    if x == ">":
        roboSantaPositionX += 1
    if x == "v":
        roboSantaPositionY += -1
    if x == "^":
        roboSantaPositionY += 1
    coordinate = (str(roboSantaPositionX) + "," + str(roboSantaPositionY))
    roboSantaCoordinateList.append(coordinate)

combinedList = roboSantaCoordinateList + santaCoordinateList

combinedList = list(set(combinedList))

for y in combinedList:
    houses += 1

print(houses)