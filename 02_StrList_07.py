x = input()
a = x[3::7]
b = x[7::5]
c = str((int(a)+int(b)+10000)//10%1000)
d = (int(c[0])+int(c[1])+int(c[2]))%10 + 1
f = "ABCDEFGHIJ"
g = f[d-1]
print(c+g)