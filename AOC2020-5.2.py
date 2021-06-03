
highSeatID = 0 # to hold 'current' highest seat ID during execution

# Since 5.1 answer returns 801 as 'highest Seat ID'....
seatIDList = list(range(1,802)) # to hold a list of all possible seat IDs

def search(value, list):
    for i in range(len(list)):
        if list[i] == value:
            return True
    return False


f = open("AOC2020-5.1(input).txt")
for line in f:
    # reset row/column values
    row = ""
    column = ""
    # convert row and column into 'binary string' 
    for element in line:
        if element == 'F':  row += '0'
        if element == 'B':  row += '1'
        if element == 'R':  column += '1'
        if element == 'L':  column += '0'
    # convert row and column from 'binary string' -> 'integer'
    row = int(row, 2)
    column = int(column, 2)
    # find out seat ID value, then compare with highSeatID. 
    # If greater than highSeatID, update highSeatID with new highest value
    seatID = row * 8 + column
    if seatID > highSeatID:  highSeatID = seatID

    ### Stage 2 ###

    # We've 'seen' this particular row/column/seatID combination, so that can't be our seat
    try:
        seatIDList.remove(seatID)    # the seatID value that 'remains' must be our seat
    except:
        # we've already removed this seatID (shouldn't happen in theory) - so report problem and continue
        print("DEBUG: Already removed seatID %i" % seatID)
        continue


print("highest Seat ID is: %i" % highSeatID)
for seats in seatIDList:
    # is there a seatID either side of seats? If so, that's not our seat and we can ignore it
    if not(search(seats-1, seatIDList) or search(seats+1, seatIDList)):
        print("My seatID is %i" % seats)


