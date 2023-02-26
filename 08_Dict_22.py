x = {}
y = {}
for i in range(int(input())) :
    ice,price = input().split()
    x[ice] = float(price)
for i in range(int(input())) :
    ice2,n = input().split()
    if ice2 in x :
        if ice2 in y : y[ice2] += x[ice2]*float(n) 
        else : y[ice2] = x[ice2]*float(n)
if len(y) != 0 :
    c = 0
    t = []
    for e in y.values() : c += e
    for a,b in y.items() : t.append([b,a])
    t.sort() ; t = t[::-1]
    o = [t[0][1]]
    for i in range(len(t)-1) :
        if t[i][0] == t[i+1][0] : o.insert(0,t[i+1][1])
        else : break
    print("Total ice cream sales:",c)
    print("Top sales:",", ".join(o))
else : print("No ice cream sales")