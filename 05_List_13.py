x = []
for i in range(int(input())) : x += [int(input())]
x += [int(e) for e in input().split()]
i = 0
while i != -1 :
    y = int(input())
    if y != -1 : x.append(y)
    else : break
y = []
for i in range(len(x)) :
    if i%2 == 0 :
        y.append(x[i])
    else :
        y.insert(0,x[i])
print(y)