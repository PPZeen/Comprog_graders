ansli = []
errli = []
while True :
    ss = input()
    err = 0
    if ss=='END' : break
    else:
        s = ss.split()
        numb,typ,d,m,y = s[0],s[1],int(s[2]),int(s[3]),int(s[4])
        if y<2558 and err == 0: 
            errli.append("Error: "+ss+' --> Invalid year')
            err = 1
        if (not 0<m<13) and err == 0 : 
            errli.append("Error: "+ss+' --> Invalid month')
            err = 1
        if (y-543)%400==0 or ((y-543)%4==0 and (y-543)%100!=0) : xx=29
        else : xx=28
        date = [31,xx,31,30,31,30,31,31,30,31,30,31]
        if err == 0 and (d<1 or d>date[m-1]) :
            errli.append("Error: "+ss+' --> Invalid date')
            err = 1
        if typ not in 'EQNF' and err == 0:
            errli.append("Error: "+ss+' --> Invalid delivery type')
            err = 1
    if err == 0:
        stt = numb+': delivered on '
        if typ == 'E' : d += 1
        if typ == 'Q' : d += 3
        if typ == 'N' : d += 7
        if typ == 'F' : d += 14
        if d>date[m-1]:
            d-=date[m-1]
            m+=1
        if m>12 :
            m-=12
            y+=1 
        stt = stt + str(d) + '/' + str(m) + '/' + str(y)
        ansli+=[[y,m,d,stt]]
for e in errli: print(e)
ansli.sort()
for e in ansli: print(e[3])