def spiral_square(n): # n is a positive odd number
    a = []
    for i in range(n+2):
        a2 = []
        for j in range(n+2): a2.append(-1)
        a.append(a2)
    for i in range(1,n+1):
        for j in range(1,n+1):
            a[i][j]=0
    i = n
    j = n
    k = n*n
    while(k>0):
        while(a[i][j]==0):
            a[i][j]=k
            k-=1
            j-=1
        j+=1
        i-=1
        while(a[i][j]==0):
            a[i][j]=k
            k-=1
            i-=1
        i+=1
        j+=1
        while(a[i][j]==0):
            a[i][j]=k
            k-=1
            j+=1
        j-=1
        i+=1
        while(a[i][j]==0):
            a[i][j]=k
            k-=1
            i+=1
        i-=1
        j-=1
    a=a[1:-1]
    q=[]
    for e in a:
        e=e[1:-1]
        q.append(e)
    return q
def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip())