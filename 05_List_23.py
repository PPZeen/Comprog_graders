phase = []
order = []
point = []
x = []
k = 0
for i in range(int(input())) :
    point.append([float(b) for b in input().split()])
    k += 1
    order.append(k)
for i in range(len(point)) :
    d = ((point[i][0])**2 + (point[i][1])**2)**0.5
    phase.append(d)
for i in range(len(point)) :
    y = [phase[i],order[i],point[i]]
    x.append(y)
x.sort()
o = x[2][1]
p = x[2][2]
print("#"+str(o)+":","("+str(p[0])+",",str(p[1])+")")