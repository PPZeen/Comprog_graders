x = input()
s = 0
p = 0
while x != "q" :
    s += float(x)
    x = input()
    p += 1
else :
    if p < 1  :
        print("No Data")
    else :    
        print(round(s/p,2))