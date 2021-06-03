import re
from operator import xor


passwords = {}

counter = 0
validPW = 0

f = open("AOC2020-2.1(input).txt")
for line in f:
    try:
        count, letter, value = line.split()
    except:
        continue
    # key = str(a) + " " + str(b)
    letter = letter[:-1]
    # passwords[key] = value
    minCount, maxCount = count.split('-')
    minCount = int(minCount)
    maxCount = int(maxCount)
    if value.count(letter) >= minCount and value.count(letter) <= maxCount:
        counter += 1
    if xor(bool(value[minCount-1] == letter), bool(value[maxCount-1] == letter)):
        validPW += 1
f.close()

print("counter = ", counter)
print("Valid PW = ", validPW)

