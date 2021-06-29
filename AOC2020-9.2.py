

def createInput(filename, datalist):

    f = open(filename)
    for line in f:
        datalist.append(int(line.strip("\n")))
    return datalist


def validData(datalist, index, dataElements):
    '''
    datalist = list of data
    index = current position in datalist
    dataElements = nummber of data elements that we use to test the data input
    '''
    testValue = datalist[index]    # the value we're trying to match
    # print(testValue)
    if index - dataElements == 0:   
        prevData = datalist[:index]
    else:
        prevData = datalist[index-dataElements:index]
    # print(prevData)
    for i in prevData:
        for j in prevData:
            if calcData(i, j, testValue):
                return True
    return False


def calcData(value1, value2, testValue):
    if value1 != value2 and (value1 + value2 == testValue):
        return True
    else:
        return False


def findContiguosSet(answer, dataset):
    '''
    answer = what we're looking for (specifically we want to find a series of number in dataset that add together to match this 'answer')
    dataset = the original dataset that was used earlier
    '''
    startCounter = 0    # start point in dataset[counter]. We may increment this as needed
    endCounter = 1    # make sure this doesn't become greater than the size of dataset
    while not addValues(dataset[startCounter:endCounter], answer):
        if len(dataset) > endCounter:    
            endCounter += 1
        else:    
            # end of dataset
            if len(dataset) > startCounter:
                startCounter += 1
                endCounter = startCounter + 1
            else:
                # end of data!!
                print("reached the end of the data - and didn't find a weakness in the crypt!")
                return
    # Found a series of numbers in dataset that sum together to equal 'answer'
    highNo = max(dataset[startCounter:endCounter])
    lowNo = min(dataset[startCounter:endCounter])
    print("Encryption Weakness = %i" % (highNo + lowNo))
    return


def addValues(subset, answer):
    # extract each value from subset and add them together. 
    # if result == answer, return True. Else, return False
    if sum(subset) == answer:
        return True
    else:
        return False


def main():

    XMASdata = []
    filename = "AOC2020-9.1(input).txt"
    dataCompareCounter = 25
    XMAScounter = dataCompareCounter

    XMASdata = createInput(filename, XMASdata)

    while validData(XMASdata, XMAScounter, dataCompareCounter):
        XMAScounter += 1
    
    print("didn't get a hit - invalid data!!")
    print(XMASdata[XMAScounter])

    findContiguosSet(XMASdata[XMAScounter], XMASdata)



if __name__ == "__main__":
    main()

