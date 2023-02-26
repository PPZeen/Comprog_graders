h = int(input())
print(" "*(h-1)+"*")
for i in range(1,h-1) :
    if h <= 3 :
        print(" "*(h-1-i)+"*"+" "*(i)+"*"*i)
    else :
        print(" "*(h-1-i)+"*"+" "*((2*i)-1)+"*")
print("*"*(2*h-1))