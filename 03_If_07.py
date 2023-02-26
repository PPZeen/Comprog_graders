n = int(input())
if n < 1000 :
    p = str(n)
elif n < 10000 :
    p = str(round(n/1000,1)) + "K"
elif n < 1000000 :
    n+=100
    n = round(n,-3)
    n = int(n/1000)
    p = str(n) + "K"
elif n < 10000000 :
    p = str(round(n/1000000,1)) + "M"
elif n < 1000000000 :
    n+=100000
    n = round(n,-6)
    n = int(n/1000000)
    p = str(n) + "M"
elif n < 10000000000 :
    p = str(round(n/1000000000,1)) + "B"
else :
    n = round(n,-9)
    n = int(n/1000000000)
    p = str(n) + "B"

print(p)