with open("Day 2\part2-Input.txt") as f:
    data = f.read()

formattedData = data.split("\n")
total = 0


for x in formattedData:
    thing = x.replace('x',' ')
    thingy = thing.split(" ")

    number1 = int(thingy[0])
    number2 = int(thingy[1])
    number3 = int(thingy[2])

    numberList = [number1,number2,number3]

    lowest1 = min(numberList)
    lowest1Index = numberList.index(lowest1)
    del numberList[lowest1Index]
    lowest2 = min(numberList)

    coverBox = ((lowest1 * 2) + (lowest2 * 2))
    ribbon = (number1 * number2 * number3)

    boxTotal = (coverBox + ribbon)

    total += boxTotal

print(total)