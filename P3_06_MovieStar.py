star = {}
n = int(input())
for i in range(n):
    s = [k.strip() for k in input().split(',')]
    if s[1] not in star : star[s[1]] = []
    if s[2] not in star : star[s[2]] = []
    star[s[1]].append(s[0])
    star[s[2]].append(s[0])
ans = [k.strip() for k in input().split(',')]
for e in ans:
    if e in star : print(e,'->',(', ').join(star[e]))
    else : print(e,'->','Not found')