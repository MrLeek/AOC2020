import re
from operator import xor
import numpy


'''
passport = {
    "ecl": "",
    "pid": "",
    "eyr": "",
    "hcl": "",
    "byr": "",
    "iyr": "",
    "cid": "",
    "hgt": ""
}
'''
passport = {}
def resetPassport():
    passport = {}

def validPassport(passport):
    # test for valid passport. return True/False as needed
    print(passport)
    if int(passport["byr"]) >= 1920 and int(passport['byr']) <= 2002:
        print("valid year")
        return True
    
    return False


valid = 0
invalid = 0

f = open("AOC2020-4.1(input).txt")
for line in f:
    # print(len(line))
    if not (line.endswith("\n") and line.startswith("\n")):
        # stuff here
        line = line.split()
        # print(line)
        for l in line:
            # print(l)
            key, value = l.split(":")
            passport[key] = value

    else:
        # empty line. End of data input, so test for value/invalid
        # print("empty line detected")
        if (len(passport) == 8) or (not "cid" in passport and len(passport) == 7):
            # print(passport)
            passport = {}
            valid += 1
            # print("valid = %i" % valid)
        else:
            # if "cid" in passport and len(passport == 7):
            #invalid 
            invalid += 1
            # print("invalid valur = %i" % invalid)
            passport = {}

print("last line")
if (len(passport) == 8) or (not "cid" in passport and len(passport) == 7):
    valid += 1
    # print("valid = %i" % valid)
else:
    #invalid
    invalid += 1
    # print("invalid valur = %i" % invalid)

print("no of valid Passports = %i" % valid)
print("no of invalid passports = %i" % invalid)


