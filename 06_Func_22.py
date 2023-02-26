def distance1(x1, y1, x2, y2) :
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return d

def distance2(p1, p2) :
    x1 = p1[0] ; x2 = p2[0]
    y1 = p1[1] ; y2 = p2[1]
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return d

def distance3(c1, c2) :
    s = False
    x = distance1(c1[0],c1[1],c2[0],c2[1])
    d = c1[2]+c2[2]
    if x <= d :
        s = True
    return x,s
    
def perimeter(points) :
    k = 0
    for i in range(len(points)-1) :
        y = distance2(points[i],points[i+1])
        k += y
    x = distance2(points[-1],points[0])
    k += x
    return k

print(distance1(0, 0, 3, 4)) 
print(distance2([0,0], [3,4])) 
a,b = distance3([0,0,1], [5,0,2]) ; print(a, b) 
print(perimeter([[0,0], [0,2], [2,2], [2,0]]))

exec(input().strip()) 