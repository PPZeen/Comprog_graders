def change(x) :
    y = ""
    for e in x :
        if e in "\"\'/\\,-_=+)(}{][><^*%!.:;" : y += " "
        else : y += e
    return y
x = change(input()).lower().split()
y = x[0]
for e in x[1::] :
    z = e[0].upper() + e[1::]
    y += z
print(y)