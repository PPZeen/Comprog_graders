import math
x = input().split(",")
a = x[0]
b = x[1]
c = x[2]
m = int(a+b)*int("9"*len(c)) + int(c)
n = int("9"*len(c)+"0"*len(b))
h = math.gcd(m,n)
print(m//h ,"/",n//h)