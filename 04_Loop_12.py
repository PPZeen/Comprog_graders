n = int(input())
y = []
for i in range(1,n+1) :
    x = input().split()
    y += x
z = input()
u = ""
v = ""
if z == "Zig-Zag" :
    for e in y[::2] :
        u += str(e)+" "
elif z == "Zag-Zig" :
    for e in y[1::2] :
        v += str(e)+" "
print(min(v))