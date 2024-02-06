with open("Day 5\part1-Input.txt") as f:
    data = f.read()

formattedData = data.split("\n")

doubleLetterInt = 0
vowel = 0
naughty = False
niceStrings = 0
doubleLetter = ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz"]
bannedStrings = ["ab","cd","pq","xy"]

for x in formattedData:
    naughty = False
    doubleLetterInt = 0
    bannedStringsInt = 0
    vowel = 0
    for y in bannedStrings:
        if y in x:
            bannedStringsInt += 1
    if bannedStringsInt > 0:
        naughty = True
    singleString = list(x)
    for y in singleString:
        if y == "a":
            vowel += 1
        if y == "e":
            vowel += 1
        if y == "i":
            vowel += 1
        if y == "o":
            vowel += 1
        if y == "u":
            vowel += 1
    if vowel < 3:
        naughty = True
    for y in doubleLetter:
        if y in x:
            doubleLetterInt += 1
    if doubleLetterInt < 1:
        naughty = True
    if naughty is False:
        niceStrings += 1

print(niceStrings)