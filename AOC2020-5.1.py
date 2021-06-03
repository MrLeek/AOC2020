


highSeatID = 0 # to hold 'current' highest seat ID during execution

f = open("AOC2020-5.1(input).txt")
for line in f:
    # split the line into two
    # row = line[:7]
    # column = line[-3:]
    row = ""
    column = ""
    # convert row and column into binary -> decimal
    for element in line:
        if element == 'F':  row += '0'
        if element == 'B':  row += '1'
        if element == 'R':  column += '1'
        if element == 'L':  column += '0'
    # convert row and column from 'binary string' -> 'integer'
    #print(row, column)
    row = int(row, 2)
    column = int(column, 2)
    #print(row, column)
    # find out seat ID value, then compare with highSeatID. 
    # If greater than highSeatID, update highSeatID with new highest value
    seatID = row * 8 + column
    if seatID > highSeatID:  highSeatID = seatID

print("highest Seat ID is: %i" % highSeatID)

