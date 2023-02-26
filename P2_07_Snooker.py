def score(s):
    ans = 0
    for e in s:
        if e == 'R' : ans+=1
        if e == 'Y' : ans+=2
        if e == 'G' : ans+=3
        if e == 'W' : ans+=4
        if e == 'B' : ans+=5
        if e == 'P' : ans+=6
        if e == 'K' : ans+=7
    return ans
sc1=0
sc2=0
while True:
    s=input()
    if s[0]=='1' : sc1+=score(s)
    if s[0]=='2' : sc2+=score(s)
    if s[1]=='K' : break
print(sc1,sc2)
if sc1>sc2 : print("Player 1 wins")
elif sc1<sc2 : print("Player 2 wins")
else : print("Tie")