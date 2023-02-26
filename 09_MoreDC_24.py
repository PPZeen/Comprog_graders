R = {}
animallist = []
while True :
    s = input().split(', ')
    if len(s) == 1 : break
    if s[1] not in animallist : 
        animallist.append(s[1])
        R[s[1]] = []
    R[s[1]].append(s[0])
for e in animallist:
    print(e+':',', '.join(R[e]))