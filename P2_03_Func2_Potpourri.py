def convex_polygon_area(p):
    ans=0
    for i in range(len(p)):
        ans = ans + p[i-1][0]*p[i][1] - p[i][0]*p[i-1][1]
    if ans >=0 : return ans*0.5
    else : return -ans*0.5
def is_heterogram(s):
    k = s.lower()
    char='abcdefghijklmnopqrstuvwxyz'
    p={}
    for e in char: p[e]=0
    for e in k: 
        if e in p: p[e]+=1
    for e in p:
        if p[e]>1: return False
    return True
def replace_ignorecase(s, a, b):
    st = s.lower()
    st2 = s
    oldword = a.lower()
    newword = b.lower()
    lenold = len(oldword)
    lennew = len(newword)
    i = 0
    while True:
        k = st.find(oldword,i,)
        if k == -1 : return st2
        else :
            st = st[0:k]+b+st[k+lenold:]
            st2 = st2[0:k]+b+st2[k+lenold:]
            i += lennew
def top3(votes):
    li = [[votes[e],e] for e in votes]
    li.sort(reverse=1)
    for j in range(len(li)-1):
        for i in range(len(li)-1-j):
            if li[i][0]==li[i+1][0] and li[i][1]>li[i+1][1]: li[i],li[i+1]=li[i+1],li[i]
    li = li[0:3]
    return [k[1] for k in li]
for k in range(2):
    exec(input().strip())