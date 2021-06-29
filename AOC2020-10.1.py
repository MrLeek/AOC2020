

def createInput(filename, datalist):
    f = open(filename)
    for line in f:
        datalist.append(int(line.strip("\n")))
    datalist = sorted(datalist)
    return datalist


def findAdaptors(adaptorlist):
    global oneJoltCounter, twoJoltCounter, threeJoltCounter
    startPoint = 0
    for item in adaptorlist:
        if startPoint + 1 == item:
            oneJoltCounter += 1
            startPoint += 1
        elif startPoint + 2 == item:
            twoJoltCounter += 1
            startPoint += 2
        elif startPoint + 3 == item:
            threeJoltCounter += 1
            startPoint += 3
    # last device is always rated for 3 jolts higher, so add one to threeJoltCounter
    threeJoltCounter += 1


# global variables
oneJoltCounter = 0
twoJoltCounter = 0    
threeJoltCounter = 0


def main():

    joltageInput = []
    filename = "AOC2020-10(input).txt"
    joltage = 0

    joltageInput = createInput(filename, joltageInput)

    findAdaptors(joltageInput)

    print("one jolt counter = %i" % oneJoltCounter)
    print("two jolt counter = %i" % twoJoltCounter)
    print("three jolt counter = %i" % threeJoltCounter)
    print("result is = %i" % (oneJoltCounter * threeJoltCounter))




if __name__ == "__main__":
    main()

