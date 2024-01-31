with open("Day 1\part1-input.txt") as f:
    data = f.read()

floor = 0

for x in data:
    if x == "(":
        floor += 1
    if x == ")":
        floor -= 1

print(floor)
