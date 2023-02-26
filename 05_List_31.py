x = input().split()
N = int(len(x)/2)
y = input()
z = ""
for i in range(len(y)) :
    if y[i] == "C" :
        a = x[:N:]
        b = x[N::]
        x = b+a
    elif y[i] == "S" :
        a = x[:N:]
        b = x[N::]
        i = 1
        for e in b :
            a.insert(i,e)
            i += 2
        x = a
for i in range(len(x)) :
    z += x[i] + " "
print(z)