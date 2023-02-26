allfile = {}
ans = []
n = int(input())
for i in range(n):
    name = input()
    data = input().split()
    allfile[name] = data
while True:
    s = input()
    if s=='-1': break
    maxval = 0
    namemax = 'NOT FOUND'
    for e in allfile:
        allword = len(allfile[e])
        countword = allfile[e].count(s)
        uniqueword = set()
        for k in allfile[e]: uniqueword.add(k)
        nunique = len(uniqueword)
        point = (countword/allword)/nunique
        if point>maxval:
            maxval = point
            namemax = e
    print(namemax)