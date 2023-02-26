opr = input()
st = []
n = int(input())
chck = 1
for i in range(0,n) :
    st += [input()]
for i in range(len(st)):
    if len(st[i]) != len(st[i-1]) :
        print("Invalid size")
        chck = 0
        break
if chck == 0 :
    pass
else :
    lenx = len(st[0])
    leny = len(st)
    if opr == '90' :
        for j in range(lenx):
            for i in range(leny-1,-1,-1):
                print(st[i][j],end='')
            print()
    elif opr == 'flip' :
        for i in range(0,leny) :
            for j in range(lenx-1,-1,-1):
                print(st[i][j],end='')
            print()
    elif opr == '180' :
        for i in range(leny-1,-1,-1) :
            for j in range(lenx-1,-1,-1) :
                print(st[i][j],end='')
            print()