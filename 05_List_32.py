k = 0
nx = 0
q = []
ans = []
avgq = 0
navgq = 0
n = int(input())
for i in range(0,n) :
    c = input().split()
    if c[0] == 'reset' :
        k = int(c[1])
        nx = int(c[1])

    elif c[0] == 'new' :
        q += [ [k,int(c[1])] ]
        ans += ['ticket '+str(k)]
        k+=1

    elif c[0] == 'next' :
        ans += ['call '+str(nx)]
        nx += 1

    elif c[0] == 'order' :
        for j in range(len(q)):
            if q[j][0] == nx-1 :
                q[j]+=[int(c[1])]
                ll = int(q[j][2])-(q[j][1])
                ans += ['qtime '+str(q[j][0])+' '+str(ll)]
                avgq += ll
                navgq += 1
                break

    elif c[0] == 'avg_qtime' :
                ans += ['avg_qtime '+str(round(avgq/navgq,4))]
                
for i in range(len(ans)):
    print(ans[i])
        