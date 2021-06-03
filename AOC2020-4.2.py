import re

passport = {}

def eyeColour(value):
    # print(value)
    if value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
        return True
    else:
        # print(value)
        return False

def validPassport(passport):
    # test for valid passport. return True/False as needed
    # print(passport)
    if not (int(passport["byr"]) >= 1920 and int(passport['byr']) <= 2002):
        return False
    if not(int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020):
        return False
    if not(int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030):
        return False
    height = int(passport['hgt'][:-2])
    if not(((re.search('cm', passport['hgt']) and (150 <= height <= 193)))):
        if not((re.search('in', passport['hgt']) and (50 <= height <= 76))):
            return False
    if not(re.fullmatch(r"^#[a-f0-9A-F]{6}$", passport['hcl'])):
        return False
    if not(eyeColour(passport['ecl'])):
        return False
    if not(re.match(r"^[0-9]{9}$", passport['pid']) and (len(passport['pid']) == 9)):
        return False
    
    return True

valid = 0
invalid = 0

f = open("AOC2020-4.1(input).txt")
for line in f:
    if not (line.endswith("\n") and line.startswith("\n")):
        # stuff here
        line = line.split()
        for l in line:
            # print(l)
            key, value = l.split(":")
            passport[key] = value

    else:
        # empty line. End of data input, so test for value/invalid
        if (len(passport) == 8) or (not "cid" in passport and len(passport) == 7):
            if validPassport(passport):
                valid += 1
            else:
                invalid += 1
        else:
            invalid += 1
            # print("invalid valur = %i" % invalid)
        passport = {}

# no more lines to process, but there's one final passport record to validate...
if (len(passport) == 8) or (not "cid" in passport and len(passport) == 7):
    if validPassport(passport):
        valid += 1
    else:
        invalid += 1
else:
    #invalid
    invalid += 1

print("no of valid Passports = %i" % valid)
print("no of invalid passports = %i" % invalid)


