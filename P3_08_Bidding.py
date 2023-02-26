product = {}
pe = {}
for i in range(int(input())) :
    x = input().split()
    if x[1] not in pe : pe[x[1]] = {"price":0,"pr":[]}
    if x[0] == "B" :
        if x[2] not in product : product[x[2]] = [(x[1],int(x[3]))]
        else : product[x[2]].append((x[1],int(x[3])))
    elif x[0] == "W" :
        if x[2] in product :
            p = product[x[2]]
            for j in range(len(p)) :
                if p[j][0] == x[1] :
                    product[x[2]].remove(p[j])
                    break
for key in product :
    a = product[key]
    if a != [] :
        amax = a[0][1]
        e = a[0]
        for k in range(1,len(a)) :
            if a[k][1] > amax :
                amax = a[k][1]
                e = a[k]
        pe[e[0]]["price"] += e[1]
        pe[e[0]]["pr"].append(key)
for u in sorted(list(pe)) :
    if pe[u]["price"] == 0 : print(u+": "+"$"+str(pe[u]["price"]))
    else : print(u+": "+"$"+str(pe[u]["price"])+" -> "+" ".join(sorted(pe[u]["pr"])))   