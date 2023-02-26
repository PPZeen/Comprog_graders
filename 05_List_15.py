s = input()
s = [int(e) for e in s.split()]
s.sort()
ans = []
for i in range(len(s)) :
    if i == 0:
        ans += [s[i]]
    else :
        if s[i] != s[i-1] :
            ans += [s[i]]
anscut = ans[0:10]
print(len(ans))
print(anscut)