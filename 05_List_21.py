x = ""
y = []
s = []
ids = []
grades = []
while x != "q" :
    s.append(input())
    x = str(s[-1])
s.remove(s[-1])

uids = input().split()
for i in range(len(s)) : y += s[i].split()
for i in range(0,len(y),2) : ids.append(y[i])
for i in range(1,len(y),2) : grades.append(y[i])
for e in uids :
    if e in ids :
        z = ids.index(e)
        if grades[z] == "A" : grades[z] = "A"
        elif grades[z] == "B+" : grades[z] = "A"
        elif grades[z] == "B" : grades[z] = "B+"
        elif grades[z] == "C+" : grades[z] = "B"
        elif grades[z] == "C" : grades[z] = "C+"
        elif grades[z] == "D+" : grades[z] = "C"
        elif grades[z] == "D" : grades[z] = "D+"
        elif grades[z] == "F" : grades[z] = "D"
for i  in range(len(s)) :
    print(ids[i],grades[i])