def reverse(x) :
    y = {}
    for key in x : y[x[key]] = key
    return y
x = {}
for i in range(int(input())) :
    name,lastname,tel = input().split()
    x[name+" "+lastname] = tel
z = reverse(x)
ans = ""
for i in range(int(input())) :
    y = input().strip()
    if y in x : ans += y+" --> "+x[y]+"\n"
    elif y in z : ans += y+" --> "+z[y]+"\n"
    else : ans += y +" --> Not found\n"
print(ans)


#ans = {}
#for i in range(int(input())) :
#    y = input().strip()
#    if y in x : ans[y] = x[y]
#    elif y in z : ans[y] = z[y]
#    else : ans[y] = "Not found"
#for e in ans : print(e,"-->",ans[e])
