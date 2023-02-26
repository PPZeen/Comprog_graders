vote = {}
member = {}
while True:
    s = input().split()
    if len(s)==1 : break
    if s[0] not in vote : vote[s[0]] = dict()
    if s[1] not in vote[s[0]] : vote[s[0]][s[1]] = 0
    vote[s[0]][s[1]] += int(s[2])
    if s[1] not in member : member[s[1]]=0
    member[s[1]] += int(s[2])     
if s[0] == '1' :
    ans = [[b,a] for a,b in member.items()]
    ans.sort(reverse=1)
    print(', '.join([e[1] for e in ans[0:3]]))
if s[0] == '2' :
    ota = {}
    for e in vote:
        for k in vote[e] :
            if k not in ota : ota[k] = set()
            ota[k].add(e)
    ans = [[len(ota[a]),a] for a in ota]
    ans.sort(reverse=1)
    print(', '.join([e[1] for e in ans[0:3]]))
if s[0] == '3' :
    kami = {}
    for e in member : kami[e] = set()
    for e in vote :
        xkami = [[-1*b,a] for a,b in vote[e].items()]
        xkami.sort()
        kami[xkami[0][1]].add(e)
    ans = [[-1*len(kami[e]),e] for e in kami]
    ans.sort()
    print(', '.join([e[1] for e in ans[0:3]]))