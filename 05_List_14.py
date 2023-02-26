x = [float(e) for e in input().split()]
k = 0
for i in range(1,len(x)-1) :
    if x[i-1] < x[i] and x[i] > x[i+1] :
        k += 1
print(k)