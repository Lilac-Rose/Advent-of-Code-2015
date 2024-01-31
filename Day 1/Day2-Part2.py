with open("Day 1\part2-input.txt") as f:
    data = f.read()

floor = 0
position = 0

for x in data:
    position += 1
    if x == "(":
        floor += 1
    if x == ")":
        floor -= 1
    if floor <= -1:
        print(position)
        break