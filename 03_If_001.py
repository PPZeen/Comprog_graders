d, m, y = [int(e) for e in input().split()]
y -= 543
n = 31
if m==4 or m==6 or m==9 or m==11 :
    n = 30
else :
    if m == 2 :
        n = 28
        if y%400 == 0 :
            n = 29
        if y%4 == 0 and y%100 != 0 :
            n = 29
d = d + 15
if d > n :
    d = d-n
    m = m+1
if m > 12 :
    m = m-12
    y = y+1
y = y+543
print(str(d)+"/"+str(m)+"/"+str(y))