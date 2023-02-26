set1 = set()
n = int(input())
if n == 0 : liset1 = []
else : liset1 = input().split()
set1.update(liset1)
unionset = set1
intersecset = set1
for i in range(n-1):
    sett = set()
    lisett = input().split()
    sett.update(lisett)
    unionset = unionset.union(sett)
    intersecset = intersecset.intersection(sett)
print(len(unionset))
print(len(intersecset))