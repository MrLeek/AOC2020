import re
from operator import xor
import numpy



# set line pos = 0

linepos = [0, 0, 0, 0, 0]
openspace = 0
trees = [0,0,0,0,0]
currentLine = 1
increment = [1, 3, 5 ,7, 1] # number of right spaces to move

# open the file
f = open("AOC2020-3.1(input).txt")
# read in a line
treeCount = 0
for line in f:
    line = line.strip('\n')
    # get the length of the line
    linelen = len(line)
    for counter, value in enumerate(increment):
        # if linepos > len(line): linepos = linepos - len(line)
        # print(linepos[counter])
        if linepos[counter] > (linelen-1): 
            linepos[counter] = linepos[counter] - linelen
        # read character linepos from line
        linechar = line[linepos[counter]]
        # print(linechar)
        if linechar == "." : openspace += 1
        if linechar == "#": 
            trees[counter] += 1
            # print("hit a tree")
        linepos[counter] += value

trees[4] = 0
linepos[4] = 0


# open the file
f = open("AOC2020-3.1(input).txt")
# read in a line
for line in f:
    if currentLine == 1:
        # print(line)
        line = line.strip('\n')
        # get the length of the line
        linelen = len(line)
        # if linepos > len(line): linepos = linepos - len(line)
        if linepos[4] > (linelen-1): 
            linepos[4] = linepos[4] - linelen
        # read character linepos from line
        linechar = line[linepos[4]]
        # print(linechar)
        if linechar == "." : openspace += 1
        if linechar == "#": 
            trees[4] += 1
            # print("hit a tree")
        linepos[4] += 1
        currentLine += 1
    else:
        # print(currentLine)
        currentLine = 1

print(trees)
print(numpy.prod(trees))
