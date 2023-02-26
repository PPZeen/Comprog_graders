x = input()
y = "06","08","09"
z = x[0]+x[1]
if len(x) == 10 :
    if z in y :
        print("Mobile number")
    else :
         print("Not a mobile number")
else :
    print("Not a mobile number")