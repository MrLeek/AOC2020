import string

dict = {}
for letter in string.ascii_lowercase:
    dict[letter] = 0

sum = 0   # hold total count of all 'yes' answers
groupCount = 0    # number of people in each 'group' of respondees

f = open("AOC2020-6.1(input).txt")
for line in f:
    if not (line.endswith("\n") and line.startswith("\n")):
        # process the entries for this group
        groupCount += 1
        line = line.strip('\n')
        # print(line)
        for l in line:
            dict[l] += 1

    else:
        # empty line = end of group. End of data input, so test for value/invalid
        for each in dict:
            if dict[each] == groupCount:    # only count answers given by everyone in the group
                sum += 1
        # now reset the dictonary for the next group of answers...
        for each in dict:
            dict[each] = 0
        groupCount = 0

# no more lines to process, but there's one final record to process...
for each in dict:
    if dict[each] == groupCount:
        sum += 1
# now reset the dictonary for the next group of answers...
for each in dict:
    dict[each] = 0

print("total sum = %i" % sum)

