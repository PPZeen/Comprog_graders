import math
bd, bm, by, d, m, y = [int(e) for e in input().split()]
n = 28
q = 28
u = 365
o = 365
xd = 0
yd = 0
xdy = (y-by-1)*365
if by%4 == 3 :
    n = 29
    o = 366
if bm == 1 : xd = o-bd
elif bm == 2 : xd = o-(31+bd)
elif bm == 3 : xd = o-(n+31+bd)
elif bm == 4 : xd = o-(n+62+bd)
elif bm == 5 : xd = o-(n+92+bd)
elif bm == 6 : xd = o-(n+123+bd) 
elif bm == 7 : xd = o-(n+153+bd) 
elif bm == 8 : xd = o-(n+184+bd)
elif bm == 9 : xd = o-(n+215+bd)
elif bm == 10 : xd = o-(n+245+bd)
elif bm == 11 : xd = o-(n+276+bd)
elif bm == 12 : xd = o-(n+306+bd)
if y%4 == 3 :
    q = 29
    u = 366
if m == 1 : yd = d
elif m == 2 : yd = 31+d
elif m == 3 : yd = q+31+d
elif m == 4 : yd = q+62+d
elif m == 5 : yd = q+92+d
elif m == 6 : yd = q+123+d 
elif m == 7 : yd = q+153+d 
elif m == 8 : yd = q+184+d
elif m == 9 : yd = q+215+d
elif m == 10 : yd = q+245+d
elif m == 11 : yd = q+276+d
elif m == 12 : yd = q+306+d
t = (xd+1)+(yd-1)+xdy
p = math.sin((2*math.pi*t)/23)
e = math.sin((2*math.pi*t)/28)
i = math.sin((2*math.pi*t)/33)
print(t,"{:.2f}".format(p),"{:.2f}".format(e),"{:.2f}".format(i))