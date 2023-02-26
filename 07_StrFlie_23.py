def file(x,y) :
    score = []
    file = open(x)
    for line in file :
        ids,sc = line.split()
        if ids[:2:] == y : score.append(float(sc))
    file.close()
    score.sort()
    return score
    
x,y = input().split()
z = file(x,y[-2::])
if z == [] : print("No data")
else : print(z[0],z[-1],sum(z)/len(z))