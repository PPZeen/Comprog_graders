n = int(input())
stds = []
ans = []
for i in range(n):
    s = input().split()
    stds.append(s)
findd = input().split()
for i in range(n):
    if findd[0] in stds[i][1:] : ans.append(stds[i])
k = 1
while(k<len(findd)):
    j = 0
    while(j<len(ans)):
        if findd[k] not in ans[j][1:]:
            ans.remove(ans[j])
            j-=1
        j+=1
    k+=1
ans.sort()
if len(ans)==0 : print('Not Found')
else :
    for e in ans:
        for k in e :
            print(k,end = ' ')
        print()