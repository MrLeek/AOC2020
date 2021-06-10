import re

def luggage(file, searchTerms, bagColours):

    bagList = []
    for bag in searchTerms:
        f = open(file, "r")
        for line in f:
            if re.search(bag, line):
                # found a match, but our bag must be inside 1+ bags
                if not(bagFilter(line) == bag):
                    # found a match - but have we already counted this line?
                    for i in range(searchTerms.index(bag)):
                        if re.search(searchTerms[i], line):    # we've seen this line before
                            break
                    # new addition to the bag list - but no duplicates allowed!!
                    if not (search(bagList, bagFilter(line)) or (search(allBagsSeen, bagFilter(line)))):
                        bagColours += 1
                        bagList.append(bagFilter(line))
                        allBagsSeen.append(bagFilter(line))
        f.close()
    return bagList, bagColours

def search(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return True
    return False

def bagFilter(line):
    # send in full line, return only the intial seed '<colour> bag' part!
    return ((line.split(" contain")[0])[:-1])

allBagsSeen = []    # list of all bags seen during this recursive search
                
def main():
    bagColours = 0 
    searchTerms = []
    searchTerms.append("shiny gold bag")     # our initial seed search variable
    filename = 'AOC2020-7.1(input).txt'
    searchTerms, bagColours = luggage(filename, searchTerms, bagColours)
    
    while len(searchTerms) > 0:
        searchTerms, bagColours = luggage(filename, searchTerms, bagColours)
    
    print("total no of bag colours = %i" % bagColours)

if __name__ == "__main__":
    main()

