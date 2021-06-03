
set1 = {1721, 979, 366, 299, 675,1456}
set2 = {1721, 979, 366, 299, 675,1456}

for s in set1:
    for t in set2:
        answer = s + t
        if answer == 2020: 
            print ("found it")
            print (s, t, s+ t)

print("the end!")


with open("AOC2020-1.1(input).txt") as f:
   set1 = []
   set2 = []
   set3 = []
   lines = f.readlines()
   print(lines)
   for l in lines:
       as_list = l.split(",")
       print(as_list)
       set1.append((int(as_list[0].replace("\n", ""))))
       set2.append((int(as_list[0].replace("\n", ""))))
       set3.append((int(as_list[0].replace("\n", ""))))

for s in set1:
    for t in set2:
        for u in set3:
            answer = s + t + u
            if answer == 2020: 
                print ("found it")
                print (s, t, u, s + t + u , s * t * u)
