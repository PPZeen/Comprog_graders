x = input()
y = x.split("/")
m = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(m[int(y[1])-1] , y[0]+",",y[2])