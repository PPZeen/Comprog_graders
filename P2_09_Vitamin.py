n = int(input())
fruitlist = []
for i in range(n):
    fruitlist.append(input().split())
for e in fruitlist:
    for i in range(1,len(e)) : e[i] = float(e[i])
s = input().split()
if s[0]=='show':
    for e in fruitlist:
        for k in e: print(k,end=' ')
        print()
elif s[0]=='get':
    found = 0
    for e in fruitlist:
        if e[0]==s[1] :
            found = 1
            for k in e: print(k,end=' ')
    if found == 0: print(s[1],'not found')
elif s[0]=='avg':
    a = int(s[1])
    vitalist = [e[a] for e in fruitlist]
    print(round(sum(vitalist)/len(vitalist),4))
elif s[0]=='max':
    a = int(s[1])
    vitalist = [e[a] for e in fruitlist]
    maxx = max(vitalist)
    fruitlist.sort()
    for e in fruitlist:
        if e[a]==maxx:
            print(e[0],e[a])
            break
elif s[0]=='sort':
    a = int(s[1])
    vitalist = [[e[a],e[0]] for e in fruitlist]
    vitalist.sort()
    ansli = [kk[1] for kk in vitalist]
    for e in ansli: print(e,end=' ')