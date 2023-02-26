def pattern1(nrows, ncols):
    tab = []
    k=1
    for i in range(nrows):
        subtab = []
        for j in range(ncols):
            subtab.append(k)
            k+=1
        tab.append(subtab)         
    return tab

def pattern2(nrows, ncols):
    tab = []
    for i in range(nrows):
        subtab = [nrows*n-i for n in range(1,ncols+1)]
        tab.append(subtab)
    tab.sort()
    return tab
def pattern3( N ):
    tab = []
    k=1
    for i in range(N):
        subtab = [0]*i
        for j in range(i,N):
            subtab.append(k)
            k+=1
        tab.append(subtab)
    return tab
def pattern4( N ):
    tab = []
    k=1
    for i in range(N):
        subtab = [0]*(N-i-1)
        for j in range(N-i-1,N):
            subtab.append(k)
            k+=1
        tab.append(subtab)
    tab2 = []
    for i in range(N):
        subtab2 = []
        for j in range(N):
            subtab2.append(tab[j][-1-i])
        tab2.append(subtab2)
    return tab2
def pattern5( N ):
    tab = []
    k=1
    kk=1
    nn = N
    for i in range(N):
        subtab = [0]*i
        while True:
            if len(subtab)==N: break
            else :
                subtab.append(k)
                k+=nn
                nn-=1
        tab.append(subtab)
        kk+=1
        k=kk
        nn=N
    return tab
def pattern6( N ):
    tab = []
    if N==0 : return tab
    for i in range(N):
        tab.append([])
        for j in range(N):
            tab[i].append(0)
    i = 0
    j = 0
    x = 1
    while(not(i==0 and j==N-1)):
        while (j<N):
            tab[i][j] = x
            x += 1
            i+=1
            j+=1
        i-=2
        j-=1
        if(i==0 and j==N-1): break
        while (i>-1):
            tab[i][j] = x
            x += 1
            i-=1
            j-=1
        i+=1
        j+=2
    tab[i][j] = x
    return tab
exec(input().strip())