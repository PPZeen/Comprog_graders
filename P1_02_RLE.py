x = input()
if x == "str2RLE" :
    y = input()
    c = ""
    k = 1
    for i in range(len(y)-1) :
        if y[i] == y[i+1] :
            k += 1
        else :
            c += y[i]+" "+str(k)+" "
            k = 1
    print(c)
elif x == "RLE2str" :
    a = input().split()
    b = ""
    for i in range(0,len(a)-1,2) :
       b += a[i]*int(a[i+1])
    print(b)
else : print("Error")
   