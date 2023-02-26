n = input()
i = 0
while len(n.split())>1 :
    if i%2 == 0:
        a,b=[int(e) for e in n.split()]
    else :
        b,a=[int(e) for e in n.split()]
    if i == 0:
        mnx=a
        mxx=a
        mny=b
        mxy=b
    mnx = min(mnx,a)
    mxx = max(mxx,a)
    mny = min(mny,b)
    mxy = max(mxy,b)
    n = input()
    i+=1
if n == 'Zig-Zag' :
    print(mnx,mxy)
else :
    print(mny,mxx)