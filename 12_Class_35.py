hu = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
te = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
on = ['','I','II','III','IV','V','VI','VII','VIII','IX']
class roman :
    def __init__(self, r):
        self.thou = 0
        self.hund = 0
        self.tens = 0
        self.ones = 0
        k = r
        if len(k)>0:
            i=0
            while(True):
                if i==len(k): break
                if k[i] != 'M': break
                i+=1
            self.thou += len(k[0:i])
            k = k[i:]
            if 'CM' in k: i=9
            elif 'CD' in k: i=4
            else :
                for i in range(9,-1,-1):
                    if hu[i] in k: break
            self.hund += i
            k = k[len(hu[i]):]
            if 'XC' in k: i=9
            elif 'XL' in k: i=4
            else:
                for i in range(9,-1,-1):
                    if te[i] in k: break
            self.tens += i
            k = k[len(te[i]):]
            if 'IX' in k: i=9
            elif 'IV' in k: i=4
            else :
                for i in range(9,-1,-1):
                    if on[i] in k: break
            self.ones += i
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    def __str__(self):
        return self.thou*'M'+hu[self.hund]+te[self.tens]+on[self.ones]
    def __int__(self):
        return 1000*self.thou+100*self.hund+10*self.tens+self.ones
    def __add__(self, rhs):
        c = roman('')
        c.ones = self.ones + rhs.ones
        c.tens = self.tens + rhs.tens
        c.hund = self.hund + rhs.hund
        c.thou = self.thou + rhs.thou
        if c.ones>10:
            c.ones-=10
            c.tens+=1
        if c.tens>10:
            c.tens-=10
            c.hund+=1
        if c.hund>10:
            c.hund-=10
            c.thou+=1
        return c
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))