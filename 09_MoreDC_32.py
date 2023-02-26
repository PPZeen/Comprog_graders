def first_fit(L, e):
    check = False
    for i in range(len(L)):
        if sum(L[i])+e<=100 :
            L[i].append(e)
            check = True
            break
    if not check :
        L.append([e])
def best_fit(L, e):
    k = []
    for i in range(len(L)):
        k.append([sum(L[i]),i])
    k.sort(reverse=1)
    check = False
    for i in range(len(k)):
        if k[i][0]+e<=100 :
            L[k[i][1]].append(e)
            check = True
            break   
    if not check : L.append([e])
def partition_FF(D): 
    L = []
    for e in D:
        first_fit(L,e)
    return L
def partition_BF(D):
    L = []
    for e in D:
        best_fit(L,e)
    return L
exec(input().strip())