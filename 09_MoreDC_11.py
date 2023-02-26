n = int(input())
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j]!='.' : break
    k = (j+1)//2
    ss = '.'*k+s[j:]
    print(ss)