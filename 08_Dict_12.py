def reverse(x) :
    y = {}
    for e in x.items() :
        y[e[1]] = e[0]
    return y
x = {}
for i in range(int(input())) :
    k,v = input().split()
    x[k] = v
z = reverse(x)
pri = []
for i in range(int(input())) :
    y = input()
    if y in x : pri.append(x[y])
    elif y in z : pri.append(z[y])
    else : pri.append("Not found")
print("\n".join(pri))