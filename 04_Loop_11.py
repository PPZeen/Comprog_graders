w = input()
x = 1
y = 1
z = 1
s = ""
for i in range(len(w)-1) :
    if w[i] == w[i+1] :
        x += 1
    else: 
        s += w[i]+" "+str(x)+" "
        break
for e in range(len(w[x::])-1) :
    if w[x+e] == w[x+e+1] :
        y += 1
    else: break
s += w[x+e]+" "+str(y)+" "
if x + y == len(w) :
    print(s)
elif len(w[x+y::])-1 == 0:
    s += w[x+y]+" "+str(z)
    print(s)
else :
    for q in range(len(w[x+y::])-1) :
        if w[x+y+q] == w[x+y+q+1] :
            z += 1
    s += w[x+y]+" "+str(z)
    print(s)