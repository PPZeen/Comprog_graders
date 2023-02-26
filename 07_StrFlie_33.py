def read_next(f) :
    x = f.strip().split()
    if len(x) == 2 :
        return x
    return []
def read(f) :
    F = open(f)
    s = []
    for line in F :
        s.append(read_next(line))
    F.close()
    return s
file = input().split()
x = read(file[0]) + read(file[1])
x.sort()
for i in range(len(x)) :
    x[i].insert(0,x[i][0][-2::])
x.sort()
for i in range(len(x)) : x[i].remove(x[i][0])
y = []
for i in range(len(x)) : y.append(x[i][0] +" "+x[i][1])
print("\n".join(y))