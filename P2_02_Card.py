def cardvalue(st):
    c1 = ' A23456789TJQK'
    a = c1.index(st[0])
    c2 = ' CDHS'
    b = c2.index(st[1])
    return a,b

s = input().strip()
cardvalue(s)
k = [s[i:i+2] for i in range(0,len(s),2)]
ans = ''
for i in range(len(k)-1):
    cardv1,cdv1 = cardvalue(k[i])
    cardv2,cdv2 = cardvalue(k[i+1])
    if cardv1 != cardv2 :
        diff = cardv1-cardv2
    else : diff = cdv1-cdv2
    if diff>0:
        ans=ans+'+'+str(diff)
    else : ans+=str(diff)
print(ans)