def min2sec(x) :
    y = [int(e) for e in x.split(":")]
    return (y[0]*60)+y[1]
def sec2min(x) :
    y = x%60
    if y < 10 : return str(x//60)+":0"+str(x%60)
    return str(x//60)+":"+str(x%60)
s = {}
for i in range(int(input())) : 
    x = input().split(",")
    y = x[-2].strip()
    z = x[-1].strip()
    if y in s : s[y] += min2sec(z)
    else : s[y] = min2sec(z)
ans = sorted([[u,v] for v,u in s.items()], reverse = True)
ans = [[j,sec2min(k)] for k,j in ans[:3]]
for l in range(len(ans)) : print(ans[l][0],"-->",ans[l][1])