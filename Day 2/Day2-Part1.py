with open("Day 2\part1-Input.txt") as f:
    data = f.read()

uwu = 0
surfaceArea = 0
wrappingPaper = 0

formattedData = data.split("\n")

for x in formattedData:
    thing = x.replace('x',' ')
    thingy = thing.split(" ")
    fakeNumber1 = int(thingy[0])*int(thingy[1])
    fakeNumber2 = int(thingy[1])*int(thingy[2])
    fakeNumber3 = int(thingy[0])*int(thingy[2])

    math = [fakeNumber1, fakeNumber2, fakeNumber3]
    extra = min(math)

    surfaceArea = (2*(fakeNumber1+fakeNumber2+fakeNumber3))

    wrappingPaper = (surfaceArea+extra)

    uwu = uwu + wrappingPaper

print(uwu) 