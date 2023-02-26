def add(x) :
    y = ""
    for e in x :
        if e == " " : y = y
        else : y += e
    return y

def sort(x) :
    z = "0123456789abcdefghijklmnopqrstuvwxyz"
    List = []
    for i in range(len(x)) :
        List.append(z.index(x[i]))
    List.sort()
    return List
        
x = sort(add(input().lower()))
y = sort(add(input().lower()))
if x == y : print("YES")
else : print("NO")