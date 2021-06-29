

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



if __name__ == "__main__":
    main()

