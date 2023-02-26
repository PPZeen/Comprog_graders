t = input()
s = input()
d = ""
x = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in range(len(s)):
    if s[i] in x :
        d += s[i]
    elif s[i] in " \"\'.,()" :
        d += " "
m = d.split()
a = 0
for e in range(len(m)) :
    if t == m[e] :
        a += 1
print(a)