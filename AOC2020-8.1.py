import sys

# 1) take in list of instructions
# 2) initalise no of times each has been executed - i.e. set all to zero
# 3) set any global variables: acc = 0 (may be others)


# function
    # read in instruction
    # has it been run before? (i.e. is 'counter' > 0) if so, return 'finished' marker and acc value
    # otherwise.....
        # interpret what to do
            # if "acc" add/subtract value to the global acc variable, then increment IP by 1
            # if "nop" just increment IP by 1
            # if "jmp" change IP to +/- the value with the instruction
    # return new acc value and new IP

def instructionList(filename, programList):
    #take in file, return initialised list of instructions/counters to follow
    file = open(filename, 'r')
    for line in file:
        instrLine = []   # empty list to hold single instruction line
        line = line.strip()    # remove the '\n' char from end of line
        for word in line.split(" "):
            instrLine.append(word)
        instrLine[1] = int(instrLine[1])    # convert this value from string to integer
        instrLine.append(0)    # number of times this command has been run (i.e zero)
        programList.append(instrLine)
    return programList


def runInstruction(programCommand, IP, acc):
    # read in 'command', instruction pointer and accumulator value. 
    # Return changed instruction pointer and accumulator command
    # exit script in this function if command has been run before.
    if commandRun(programCommand):
        print("this command has been executed before!")
        print(programCommand)
        print ("Accumulator value = %i" % acc)
        sys.exit()
    else:    # 1st time to run this command!
        # print(programCommand)
        if programCommand[0] == "acc":
            acc = valueChange(acc, programCommand[1])
            IP += 1
            return acc, IP
        if programCommand[0] == "nop":
            IP += 1
            return acc, IP
        if programCommand[0] == "jmp":
            IP = valueChange(IP, programCommand[1])
            return acc, IP


def valueChange(pointer, value):
    # change value of acc by value
    pointer += value
    return pointer


def commandRun(programCommand):
    # if command has been executed before, return True. Otherwise False
    if programCommand[2] == 0:
        programCommand[2] = 1
        return False
    else:
        return True    


programList = []

def main():
    filename = 'AOC2020-8.1(input).txt'
    accumulator = 0
    instrPointer = 0
    
    instructionList(filename, programList)
    # programList now initialised with 'the program to run' - so now execute 'each command'
    while True:
        accumulator, instrPointer = runInstruction(programList[instrPointer], instrPointer, accumulator)


if __name__ == "__main__":
    main()