def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    a = len(A)
    b = len(A[0])
    for i in range(a) :
        for j in range(b) :
            A[i][j] *= c
    return A
    
def mult(A, B):
    row_A = len(A)
    cor_A = len(A[0])
    row_B = len(B)
    cor_B = len(B[0])
    ANS = []
    for i in range(row_A) :
        k = 0
        z = []
        ans = []
        for j in range(cor_A) :
            z.append(A[i][j])
        for u in range(cor_B) :
            for v in range(row_B) :
                k += z[v]*B[v][u]
            ans.append(k)
            k = 0
        ANS.append(ans)
    return ANS

#A=read_matrix();print(mult_c(0.5,A))
A=read_matrix();B=read_matrix();print(mult(A,B))
#exec(input().strip()) 