fname = input().strip()
k = int(input())
ruler = ''
for i in range(k//10) :
    ruler += '-'*9 + str(i+1)
if k%10 != 0 : 
    ruler += '-'*( k%10 )
print(ruler)
fn = open(fname)
alltext = ''
for line in fn:
    line = line.strip()
    alltext += (line+'.')
alltext = alltext[:-1]
while(alltext != ''):
    q = len(alltext)
    if q<=k :
        print(alltext.strip('.'))
        break
    elif alltext[k] == '.':
        print(alltext[0:k].strip('.'))
        alltext = alltext[k:].strip('.')
    else :
        cuttext = alltext[0:k]
        for j in range(k-1,-1,-1):
            if cuttext[j] =='.' : break
        if j>0:
            print(alltext[0:j].strip('.'))
            alltext = alltext[j:].strip('.')
        else :
            finddot = alltext.find('.')
            if finddot == -1:
                print(alltext)
                break
            else :
                print(alltext[0:finddot].strip('.'))
                alltext = alltext[finddot:].strip('.')