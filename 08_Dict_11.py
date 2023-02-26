def reverse(d) :
    newd = { }
    for e in d.items() :
        newd[e[1]] = e[0]
    return newd

def keys(d,y) :
    x = []
    for e in d.items() :
        if e[1] == y : x.append(e[0])
    return x

print(reverse({3:"A", 2:"B"}) == {"A":3, "B":2})
print(keys({3:33, 4:33, 5:55, 2:33}, 33))
print(keys({3:33, 4:33, 5:55, 2:33}, 9999)) 