def row_number(t, e):
    x = []
    for i in range(len(t)) : x += t[i]
    y = x.index(e)
    z = y//len(t)
    return z

def flatten(t):
    x = []
    for i in range(len(t)) : x += t[i]
    x.remove(0)
    return x

def inversions(x):
    n = len(x)
    k = 0
    for i in range(n) :
        for j in range(i,n) :
            if x[i] > x[j] : k += 1
    return k

def solvable(t):
    x = flatten(t)
    y = inversions(x)
    z = row_number(t, 0)
    n = len(t)
    if n % 2 != 0 :
        if y % 2 == 0 : return True
        return False
    if y % 2 != 0 :
        if z % 2 == 0 : return True
        return False
    if z % 2 != 0 : return True
    return False

print(row_number([[1,7,2,3], [6,0,8,4], [5,9,10,11], [13,14,15,12]], 0))
print(flatten([[1,7,2,3], [6,0,8,4], [5,9,10,11], [13,14,15,12]]))
print(inversions([1,7,2,3,6,8,4,5,9,10,11,13,14,15,12]))
print(solvable([[1,7,2,3], [6,0,8,4], [5,9,10,11], [13,14,15,12]]))
exec(input().strip()) 