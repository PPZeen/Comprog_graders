d = int(input())
m = int(input())
y = int(input())
ans = 0
y-=543
n=28
if (y%400)==0 :
    n=29
if ((y%4)==0) and ((y%100)!=0) :
    n=29
dateinmon = [31,n,31,30,31,30,31,31,30,31,30,31]
for i in range(m-1) :
    ans += dateinmon[i]
ans += d
print(ans)