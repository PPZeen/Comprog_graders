x = input()
if x == "str2RLE" :
    y = input() + "."
    s = ""
    k = 1
    for i in range(len(y)-1) :
        if y[i] == y[i+1] :
            k += 1
        else :
            s += y[i] + " " + str(k) + " "
            k = 1
    print(s)
elif x == "RLE2str" :
    y = input().split()
    c = ""
    for i in range(0,len(y)-1,2) :
        c += y[i]*int(y[i+1])
    print(c)
else : print("Error")