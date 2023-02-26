n = int(input())
m = n
s = []
while n != 1 :
    if n%2 == 0 : n = n//2
    else : n = 3*n + 1
    s.append(n)
s = s[-15::]
if len(s) < 15 : r = str(m)+"->"+""
else : r = ""
for i in range(len(s)) :
    if i != len(s)-1 : r += str(s[i]) + "->"
    else : r += str(s[i])
print(r)  