x = input().split()
x0 = int(x[0],2)
x1 = int(x[1],2)
y = bin(x0+x1)
print(y[2:len(y)])

