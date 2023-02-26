n = int(input())
plist = []
R = {}
for i in range(n):
    s = input().split(': ')
    plist.append(s[0])
    R[s[0]]=s[1].split(', ')
want = input()
ans = []
for e in plist:
    if e!=want:
        for ee in R[want]:
            if ee in R[e] :
                ans.append(e)
                break
if len(ans)==0 : print('Not Found')
else : 
    for e in ans:
        print(e)