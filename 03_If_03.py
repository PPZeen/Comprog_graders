a,b,c,d = [float(e) for e in input().split()]
score = (a+b+c+d-min(a,b,c,d)-max(a,b,c,d))/2
print(round(score,2))

