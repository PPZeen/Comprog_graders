import math
totalstroke = 0
tamtor = 0
sumpoint = 0
sumpar = 0
pointtable = []
cngstroke = [0]*9
for i in range(0,9) :
    s = [int(e) for e in input().split()]
    pointtable += [s]
    if pointtable[i][2] == 1:
        cngstroke[i] = min(pointtable[i][0]+2,pointtable[i][1])

for i in range(0,9) :
    tamtor += cngstroke[i]
    sumpar += pointtable[i][0]
    totalstroke += pointtable[i][1]

tamtor = 0.8*(1.5*tamtor-sumpar)
tamtor = math.floor(tamtor)
sumpoint = totalstroke - tamtor
print(totalstroke)
print(tamtor)
print(sumpoint)