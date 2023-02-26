def add_poly(p1, p2):
    li1,li2 = {},{}
    for i in range(len(p1)):
        li1[p1[i][1]]=p1[i][0]
    for i in range(len(p2)):
        li2[p2[i][1]]=p2[i][0]
    ans = dict(li1)
    for e in li2 :
        if e in ans : ans[e]+=li2[e]
        else : ans[e] = li2[e]
    ansli = []
    for e in ans:
        if ans[e] != 0 : ansli.append([e,ans[e]])
    ansli.sort(reverse=1)
    anslii = [(e[1],e[0]) for e in ansli]
    return anslii
def mult_poly(p1, p2):
    ans = {}
    li1,li2 = [],[]
    for i in range(len(p1)):
        li1.append([p1[i][1],p1[i][0]])
    for i in range(len(p2)):
        li2.append([p2[i][1],p2[i][0]])
    for i in range(len(p1)):
        for j in range(len(p2)):
            a = li1[i][0]+li2[j][0]
            b = li1[i][1]*li2[j][1]
            if a in ans : ans[a] += b
            else : ans[a] = b
    ansli = []
    for e in ans:
        if ans[e]!=0 : ansli.append([e,ans[e]])
    ansli.sort(reverse=1)
    anslii = [(e[1],e[0]) for e in ansli]
    return anslii
for i in range(3):
    exec(input().strip())