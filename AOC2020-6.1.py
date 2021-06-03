import string

dict = {}
for letter in string.ascii_lowercase:
    dict[letter] = 0

sum = 0   # hold total count of all 'yes' answers

f = open("AOC2020-6.1(input).txt")
for line in f:
    if not (line.endswith("\n") and line.startswith("\n")):
        # process the entries for this group
        line = line.strip('\n')
        for l in line:
            dict[l] += 1
            if dict[l] > 1:  dict[l]= 1    # we only count one answer from each group
    else:
        # empty line = end of group. End of data input, so test for value/invalid
        for each in dict:
            sum += dict[each]
        # now reset the dictonary for the next group of answers...
        for each in dict:
            dict[each] = 0

# no more lines to process, but there's one final record to process...
for each in dict:
    sum += dict[each]
# now reset the dictonary for the next group of answers...
for each in dict:
    dict[each] = 0

print("total sum = %i" % sum)

