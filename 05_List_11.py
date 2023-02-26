y = ["0","1","2","3","4","5","6","7","8","9"]
u = "1234567890"
s = False
for e in input()  :
    if e in u :
        if e in y : y.remove(e) ; s = True
y = ",".join(y)
if y == "" : print("None")
else : print(y)