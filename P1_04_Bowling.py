scoreboard = input()
k = []
sc = [0]*10
i = 0
while i<(len(scoreboard)):
    if len(k)<9:
        if scoreboard[i]=='X' :
            k+=['X']
            i+=1
        else :
            k+=[scoreboard[i]+scoreboard[i+1]]
            i+=2
    else :
        k+=[scoreboard[i:]]
        i+=10
m = int(input())
j = 9
while j > -1 :
    if j == 9 :
        for z in range(len(k[9])) :
            if k[j][z] == 'X' :
                sc[j] += 10
            elif k[j][z] == '/' :
                sc[j] += 10-int(k[j][z-1])
            else :
                sc[j] += int(k[j][z])
    elif j == 8 :
        if k[8]=='X' :
            sc[8] += 10
            if k[9][0]=='X' :
                sc[8] += 10
                if k[9][1] == 'X' :
                    sc[8] += 10
                else :
                    sc[8] += int(k[9][1])
            else :
                if k[9][1] != '/' :
                    sc[8] += (int(k[j+1][0])+int(k[j+1][1]))
                else :
                    sc[8] += 10
        else :
            if k[j][1] != '/' :
                sc[j] += (int(k[j][0])+int(k[j][1]))
            else :
                sc[j] += 10
                if k[j+1][0] == 'X' :
                    sc[j] += 10
                else :
                    sc[j] += int(k[j+1][0])
    else :
        if k[j]=='X' :
            sc[j] += 10
            if k[j+1]=='X' :
                sc[j] += 10
                if k[j+2][0] == 'X' :
                    sc[j] += 10
                else :
                    sc[j] += int(k[j+2][0])
            else :
                if k[j+1][1] != '/' :
                    sc[j] += (int(k[j+1][0])+int(k[j+1][1]))
                else :
                    sc[j] += 10
        else :
            if k[j][1] != '/' :
                sc[j] += (int(k[j][0])+int(k[j][1]))
            else :
                sc[j] += 10
                if k[j+1] == 'X' :
                    sc[j] += 10
                else :
                    sc[j] += int(k[j+1][0])
    j -= 1
if m in range(1,11) :
    print(sc[m-1])
else :
    totalsc = 0
    for i in range(len(sc)) :
        totalsc += sc[i]
    print(totalsc)