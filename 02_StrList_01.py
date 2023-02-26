
x = input()
a = x[0]
b = x[1]+x[2]+x[3]+x[4]
c = x[5]+x[6]+x[7]+x[8]+x[9]
d = x[10]+x[11]
e = (11-(13*int(x[0])+12*int(x[1])+11*int(x[2])+10*int(x[3])+9*int(x[4])+8*int(x[5])+7*int(x[6])+6*int(x[7])+5*int(x[8])+4*int(x[9])+3*int(x[10])+2*int(x[11]))%11)%10
print(a,b,c,d,e)