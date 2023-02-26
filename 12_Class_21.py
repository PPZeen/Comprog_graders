class Complex :
    def __init__(self,a,b):
        self.r = a
        self.c = b
    def __str__(self):
        re = self.r
        im = self.c
        if re != 0 :
            if im > 0 :
                if im == 1 : return str(re)+"+i"
                return str(re)+"+"+str(im)+"i"
            elif im < 0 :
                if im == -1 : return str(re)+"-i"
                return str(re)+str(im)+"i"
            else : return str(re)
        else :
            if im != 0 :
                if im == 1 : return "i"
                elif im == -1 : return "-i"
                return str(im)+"i"
        return "0"     
    def __add__(self,rhs):
        return Complex(self.r+rhs.r,self.c+rhs.c)
    def __mul__(self,rhs):
        a,b = self.r, self.c
        c,d = rhs.r, rhs.c 
        return Complex(a*c - b*d ,a*d + b*c)
    def __truediv__(self,rhs):
        a,b = self.r, self.c
        c,d = rhs.r, rhs.c
        return Complex(((a*c+b*d)/((c**2)+(d**2))),(-a*d+b*c)/((c**2)+(d**2)))

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)
