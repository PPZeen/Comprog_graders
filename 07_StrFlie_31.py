def R(x) :
    y = ""
    for e in x :
        if e == "A" : y += "T"
        elif e == "C" : y += "G"
        elif e == "G" : y += "C"
        elif e == "T" : y += "A"
    print(y[::-1])

def F(x) :
    A,T,G,C = 0,0,0,0
    for e in x :
        if e == "A" : A += 1
        elif e == "T" : T += 1
        elif e == "G" : G += 1
        elif e == "C" : C += 1
    print("A="+str(A)+", "+"T="+str(T)+", "+"G="+str(G)+", "+"C="+str(C))
def D(x) :
    y = input()
    k = 0
    st = 0
    while True :
        z = x.find(y,st)
        if z != -1 :
            k += 1
            st = z+1
        else : break
    print(k)
x = input().strip().upper()
y = input().strip().upper()
check = "ATGC"

for e in x :
    s = True
    if e not in check :
        print("Invalid DNA")
        s = False
        break
if s == True :
    if y == "R" : R(x)
    elif y == "F" : F(x)
    elif y == "D" : D(x)
