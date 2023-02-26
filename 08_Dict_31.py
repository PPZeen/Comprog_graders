def total(pocket):
    summ = 0
    for i in pocket : summ += i*pocket[i]
    return summ
def take(pocket, money_in):
    for i in money_in :
        if i in pocket :
            pocket[i] += money_in[i]
        else :
            pocket[i] = money_in[i]
    return pocket
def pay(pocket, amt):
    pocketl = []
    for e in pocket: pocketl.append([e,pocket[e]])
    pocketl.sort(reverse=1)
    pp = {} ; i = 0
    for e in pocketl : pp[e[0]] = 0
    while i<len(pocketl) :
        while amt>=pocketl[i][0] and pocketl[i][1]>0:
            amt -= pocketl[i][0]
            pocketl[i][1] -= 1
            pp[pocketl[i][0]] += 1
        i+=1
    pp2 = {}
    for e in pp:
        if pp[e] >0 : pp2[e] = pp[e]
    if amt > 0 : return {}
    else :
        for e in pp :
            pocket[e] -= pp[e] 
        return pp2
#exec(input().strip())

#p={100:2, 50:2, 5:2, 1:2};print(total(p))
#p={100:5};take(p,{100:2, 1:3});print(p)
#p={100:5};take(p,{100:0, 1:0});print(p)
#p={10:5, 1:7};print(pay(p, 12));print(p)
#p={10:5, 1:7};print(pay(p, 18));print(p)
#p={10:5, 1:7};print(pay(p, 100));print(p) 
p={10:5, 1:7};print(pay(p, 57));print(p) 