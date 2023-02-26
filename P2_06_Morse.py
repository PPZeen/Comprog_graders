err = 0
filename = input().strip()
fn = open(filename,'r')
code = fn.readline().strip()
if code!='T2M' and code!='M2T' :
    print('Invalid code')
    err = 1
pattern = fn.readline().strip()
if err == 0 :
    while True:
        s = fn.readline().strip()
        errr=0
        if len(s)==0 : break
        else :
            if code == 'T2M' :
                morse = ''
                for e in s :
                    j = pattern.find('[' + e + ']')
                    if j == -1 : 
                        print('Invalid :',s)
                        errr=1
                    j += 3
                    k = pattern.find('[',j)
                    morse += pattern[j:k] + ' '
                if errr==0: print(morse.strip())
            elif code == 'M2T':
                txt = ''
                ss=s.split()
                for e in ss:
                    j = pattern.find(']' + e + '[')
                    if j == -1 : 
                        print('Invalid :',s)
                        errr=1
                    txt += pattern[j-1]
                if errr==0: print(txt.strip())
fn.close()