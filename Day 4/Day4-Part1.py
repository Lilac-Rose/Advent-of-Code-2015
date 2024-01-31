import hashlib

input = "ckczppom"
number = 0

finishedHash = ""

while 1 == 1:
    fullCode = input + str(number)
    hash = hashlib.md5(fullCode.encode())
    if hash.digest().hex()[0:5] == "00000":
        break
    number += 1

print(hash.digest().hex())
print(number)