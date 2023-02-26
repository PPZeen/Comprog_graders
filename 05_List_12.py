N = int(input())
name = ["Robert","William","James","John","Margaret","Edward","Sarah","Andrew","Anthony","Deborah"]
nickname = ["Dick","Bill","Jim","Jack","Peggy","Ed","Sally","Andy","Tony","Debbie"]
L = []
x = []
for i in range (N) :
    x  += [ input()]
for e in x :
    if e in name :
        y = name.index(e)
        L.append(nickname[y])
    elif e in nickname :
        y = nickname.index(e)
        L.append(name[y])
    else :
        L += ["Not found"]
for i in range(len(x)) :
    print(L[i])